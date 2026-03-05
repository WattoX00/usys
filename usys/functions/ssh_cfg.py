from .functions import Functions
import os
import shutil
class SSHFunctions:

    @staticmethod
    def detectPackageManager():
        managers = [
            ("apt", ["apt-get", "apt"]),
            ("dnf", ["dnf"]),
            ("yum", ["yum"]),
            ("pacman", ["pacman"]),
            ("zypper", ["zypper"]),
            ("apk", ["apk"]),
            ("xbps", ["xbps-install"]),
            ("eopkg", ["eopkg"]),
            ("emerge", ["emerge"]),
            ("nix", ["nix-env"])
        ]

        for manager, binaries in managers:
            for binary in binaries:
                if shutil.which(binary):
                    return manager

        return None

    @staticmethod
    def installOpenSSH():
        manager = SSHFunctions.detectPackageManager()

        if not manager:
            print("No supported package manager detected.")
            return

        commands = {
            "apt": ["sudo", "apt-get", "update"],
            "dnf": ["sudo", "dnf", "install", "-y", "openssh-server"],
            "yum": ["sudo", "yum", "install", "-y", "openssh-server"],
            "pacman": ["sudo", "pacman", "-Sy", "--noconfirm", "openssh"],
            "zypper": ["sudo", "zypper", "install", "-y", "openssh"],
            "apk": ["sudo", "apk", "add", "openssh"],
            "xbps": ["sudo", "xbps-install", "-Sy", "openssh"],
            "eopkg": ["sudo", "eopkg", "install", "-y", "openssh"],
            "emerge": ["sudo", "emerge", "net-misc/openssh"],
            "nix": ["nix-env", "-iA", "nixpkgs.openssh"]
        }

        if manager == "apt":
            if not Functions.executeCmd(commands["apt"]):
                return
            cmd = ["sudo", "apt-get", "install", "-y", "openssh-server"]
        else:
            cmd = commands.get(manager)

        if not cmd:
            print("Unsupported package manager.")
            return

        result = Functions.executeCmd(cmd)

        if result:
            print("OpenSSH installed successfully.")

    @staticmethod
    def enableService():
        if Functions.executeCmd(["which", "systemctl"], check=False, capture=True):
            Functions.executeCmd(["sudo", "systemctl", "enable", "--now", "sshd"])
            print("SSH service enabled and started (systemd).")
            return

        if Functions.executeCmd(["which", "rc-service"], check=False, capture=True):
            Functions.executeCmd(["sudo", "rc-update", "add", "sshd"])
            Functions.executeCmd(["sudo", "rc-service", "sshd", "start"])
            print("SSH service enabled and started (OpenRC).")
            return

        if Functions.executeCmd(["which", "service"], check=False, capture=True):
            Functions.executeCmd(["sudo", "service", "ssh", "start"])
            print("SSH service started (SysVinit).")
            return

        print("Could not determine init system.")

    @staticmethod
    def generateKey():
        username = Functions.userName()

        home = f"/home/{username}"
        ssh_dir = os.path.join(home, ".ssh")
        key_path = os.path.join(ssh_dir, "id_ed25519")

        Functions.executeCmd(["sudo", "mkdir", "-p", ssh_dir])
        Functions.executeCmd(["sudo", "chmod", "700", ssh_dir])
        Functions.executeCmd(["sudo", "chown", f"{username}:{username}", ssh_dir])

        cmd = ["sudo", "-u", username, "ssh-keygen", "-t", "ed25519", "-f", key_path, "-N"]

        result = Functions.executeCmd(cmd)

        if result:
            print(f"SSH key generated for user '{username}'.")

    @staticmethod
    def setup():
        SSHFunctions.installOpenSSH()
        SSHFunctions.enableService()
