from .functions import Functions, HelpFunctions
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

        if Functions.executeCmd(cmd):
            print("OpenSSH installed successfully.")

    @staticmethod
    def enableService():

        if Functions.executeCmd(["which", "systemctl"], check=False):
            Functions.executeCmd(["sudo", "systemctl", "enable", "--now", "sshd"])
            print("SSH service enabled and started (systemd).")
            return

        if Functions.executeCmd(["which", "rc-service"], check=False):
            Functions.executeCmd(["sudo", "rc-update", "add", "sshd"])
            Functions.executeCmd(["sudo", "rc-service", "sshd", "start"])
            print("SSH service enabled and started (OpenRC).")
            return

        if Functions.executeCmd(["which", "service"], check=False):
            Functions.executeCmd(["sudo", "service", "ssh", "start"])
            print("SSH service started (SysVinit).")
            return

        print("Could not determine init system.")

    @staticmethod
    def generateKey():
        username = Functions.userName()

        home = Functions.preHomeDir(username)
        ssh_dir = os.path.join(home, ".ssh")
        key_path = os.path.join(ssh_dir, "id_ed25519")

        Functions.executeCmd(["sudo", "mkdir", "-p", ssh_dir])
        Functions.executeCmd(["sudo", "chmod", "700", ssh_dir])
        Functions.executeCmd(["sudo", "chown", f"{username}:{username}", ssh_dir])

        cmd = ["sudo", "-u", username, "ssh-keygen", "-t", "ed25519", "-f", key_path, "-N", ""]

        if Functions.executeCmd(cmd):
            print(f"SSH key generated for user '{username}'.")

    @staticmethod
    def listKeys():

        username = Functions.userName()
        ssh_dir = f"{Functions.preHomeDir(username)}/.ssh"

        if not os.path.exists(ssh_dir):
            print("No SSH directory found.")
            return []

        keys = []

        for file in os.listdir(ssh_dir):
            if file.endswith(".pub"):
                keys.append(file.replace(".pub", ""))

        if not keys:
            print("No SSH keys found.")
            return []

        print("\nAvailable SSH keys:")
        for i, key in enumerate(keys, 1):
            print(f"{i}. {key}")

        return keys

    @staticmethod
    def printPublicKey(username, key):

        pub_path = f"{Functions.preHomeDir(username)}/.ssh/{key}.pub"

        if not os.path.exists(pub_path):
            print("Public key not found.")
            return

        print("\nCopy this key to GitHub:\n")

        with open(pub_path, "r") as f:
            print(f.read())

    @staticmethod
    def setupGithubSSH():

        username = Functions.userName()
        ssh_dir = f"{Functions.preHomeDir(username)}/.ssh"

        if not os.path.exists(ssh_dir):
            print("No SSH keys found. Generating one...")
            SSHFunctions.generateKey()
            return

        keys = SSHFunctions.listKeys()

        if not keys:
            print("No keys found. Generating one...")
            SSHFunctions.generateKey()
            return

        print("\nSelect a key or generate new:")
        print("0. Generate new key")

        try:
            choice = int(input("Choice: "))
        except:
            print("Invalid choice.")
            return

        if choice == 0:
            SSHFunctions.generateKey()
            return

        if 1 <= choice <= len(keys):
            key = keys[choice - 1]
            SSHFunctions.printPublicKey(username, key)
            print("\nAdd it here:")
            print("https://github.com/settings/keys")
        else:
            print("Invalid selection.")

    @staticmethod
    def testConnection():

        print("Testing GitHub SSH connection...\n")

        Functions.executeCmd(["ssh", "-T", "git@github.com"], check=False)

    @staticmethod
    def setup():
        SSHFunctions.installOpenSSH()
        SSHFunctions.enableService()

    @staticmethod
    def helptext():
        print("""
                   SSH MANAGEMENT
        install         (i)     Install OpenSSH server
        enable          (e)     Enable and start SSH service
        setup           (s)     Run full SSH setup

                  SSH KEY MANAGEMENT
        genkey          (gk)    Generate new SSH key
        listkeys        (lk)    List existing SSH keys

                 GITHUB INTEGRATION
        github          (gh)    Setup GitHub SSH key
        test            (t)     Test SSH connection to GitHub

                    HELP & EXIT
        help            (h)     Show help menu
        quit            (q)     Quit the program
        """)

