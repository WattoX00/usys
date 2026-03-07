from .functions import Functions
import subprocess
import os
import shutil

class SambaFunctions:

    SAMBA_CONF = "/etc/samba/smb.conf"
    SHARE_BASE = "/srv/samba"

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
    def installSamba():
        manager = SambaFunctions.detectPackageManager()

        if not manager:
            print("No supported package manager detected.")
            return


        commands = {
            "apt": ["sudo", "apt-get", "update"],
            "dnf": ["sudo", "dnf", "install", "-y", "samba"],
            "yum": ["sudo", "yum", "install", "-y", "samba"],
            "pacman": ["sudo", "pacman", "-Sy", "--noconfirm", "samba"],
            "zypper": ["sudo", "zypper", "install", "-y", "samba"],
            "apk": ["sudo", "apk", "add", "samba"],
            "xbps": ["sudo", "xbps-install", "-Sy", "samba"],
            "eopkg": ["sudo", "eopkg", "install", "-y", "samba"],
            "emerge": ["sudo", "emerge", "net-fs/samba"],
            "nix": ["nix-env", "-iA", "nixpkgs.samba"]
        }

        if manager == "apt":
            if not Functions.executeCmd(commands["apt"]):
                return
            cmd = ["sudo", "apt-get", "install", "-y", "samba"]
        else:
            cmd = commands.get(manager)

        if not cmd:
            print("Unsupported package manager.")
            return

        if Functions.executeCmd(cmd):
            print("OpenSSH installed successfully.")


    @staticmethod
    def startSamba():
        cmd = ["sudo", "systemctl", "start", "smbd"]
        if Functions.executeCmd(cmd):
            print("Samba service started.")

    @staticmethod
    def stopSamba():
        cmd = ["sudo", "systemctl", "stop", "smbd"]
        if Functions.executeCmd(cmd):
            print("Samba service stopped.")

    @staticmethod
    def enableSamba():
        cmd = ["sudo", "systemctl", "enable", "smbd"]
        if Functions.executeCmd(cmd):
            print("Samba enabled at boot.")

    @staticmethod
    def disableSamba():
        cmd = ["sudo", "systemctl", "disable", "smbd"]
        if Functions.executeCmd(cmd):
            print("Samba disabled at boot.")

    @staticmethod
    def restartSamba():
        cmd = ["sudo", "systemctl", "restart", "smbd"]
        if Functions.executeCmd(cmd):
            print("Samba restarted.")

    @staticmethod
    def sambaStatus():
        cmd = ["systemctl", "status", "smbd"]
        output = Functions.executeCmd(cmd, capture=True)
        if output:
            print(output)

    @staticmethod
    def addSambaUser(username):
        print(f"Adding samba user: {username}")
        cmd = ["sudo", "smbpasswd", "-a", username]
        Functions.executeCmd(cmd, check=False)

    @staticmethod
    def removeSambaUser(username):
        cmd = ["sudo", "smbpasswd", "-x", username]
        if Functions.executeCmd(cmd):
            print(f"Samba user '{username}' removed.")

    @staticmethod
    def enableSambaUser(username):
        cmd = ["sudo", "smbpasswd", "-e", username]
        if Functions.executeCmd(cmd):
            print(f"Samba user '{username}' enabled.")

    @staticmethod
    def disableSambaUser(username):
        cmd = ["sudo", "smbpasswd", "-d", username]
        if Functions.executeCmd(cmd):
            print(f"Samba user '{username}' disabled.")

    @staticmethod
    def createShareFolder(folder):
        path = os.path.join(SambaFunctions.SHARE_BASE, folder)

        if not os.path.exists(path):
            Functions.executeCmd(["sudo", "mkdir", "-p", path])
            print(f"Folder created: {path}")
        else:
            print("Folder already exists.")

    @staticmethod
    def removeShareFolder(folder):
        path = os.path.join(SambaFunctions.SHARE_BASE, folder)

        if os.path.exists(path):
            Functions.executeCmd(["sudo", "rm", "-rf", path])
            print(f"Folder removed: {path}")

    @staticmethod
    def setFolderOwner(folder, username, group):
        path = os.path.join(SambaFunctions.SHARE_BASE, folder)
        cmd = ["sudo", "chown", "-R", f"{username}:{group}", path]
        if Functions.executeCmd(cmd):
            print(f"Ownership set to {username}:{group}")

    @staticmethod
    def setFolderPermissions(folder, perms):
        path = os.path.join(SambaFunctions.SHARE_BASE, folder)
        cmd = ["sudo", "chmod", "-R", perms, path]
        if Functions.executeCmd(cmd):
            print(f"Permissions set to {perms}")

    @staticmethod
    def addShareConfig(name, folder, valid_users="", valid_groups="", read_only="no"):
        path = os.path.join(SambaFunctions.SHARE_BASE, folder)

        config = f"""
[{name}]
   path = {path}
   browseable = yes
   read only = {read_only}
"""

        if valid_users:
            config += f"   valid users = {valid_users}\n"

        if valid_groups:
            config += f"   valid users = @{valid_groups}\n"

        try:
            with open("/tmp/samba_share.conf", "w") as f:
                f.write(config)

            Functions.executeCmd(
                ["sudo", "bash", "-c", f"cat /tmp/samba_share.conf >> {SambaFunctions.SAMBA_CONF}"]
            )

            print(f"Share '{name}' added.")
            SambaFunctions.restartSamba()

        except Exception:
            print("Failed to write samba configuration.")

    @staticmethod
    def listShares():
        try:
            with open(SambaFunctions.SAMBA_CONF, "r") as f:
                lines = f.readlines()

            for line in lines:
                if line.strip().startswith("[") and not line.strip().startswith("[global]"):
                    print(line.strip())

        except Exception:
            print("Unable to read smb.conf")

    @staticmethod
    def testConfig():
        cmd = ["testparm", "-s"]
        output = Functions.executeCmd(cmd, capture=True)
        if output:
            print(output)

    @staticmethod
    def listConnections():
        cmd = ["sudo", "smbstatus"]
        output = Functions.executeCmd(cmd, capture=True)
        if output:
            print(output)

    @staticmethod
    def folderPermissions(folder):
        path = os.path.join(SambaFunctions.SHARE_BASE, folder)
        cmd = ["ls", "-ld", path]
        output = Functions.executeCmd(cmd, capture=True)
        if output:
            print(output)

    @staticmethod
    def listSharedFiles(folder):
        path = os.path.join(SambaFunctions.SHARE_BASE, folder)
        cmd = ["ls", "-l", path]
        output = Functions.executeCmd(cmd, capture=True)
        if output:
            print(output)
