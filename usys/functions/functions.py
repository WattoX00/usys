class Functions():

    @staticmethod
    def userName(must_exist=True):
        from prompt_toolkit import PromptSession
        from ..shell.user_group_completer import UserGroupCompleter
 
        session = PromptSession(completer=UserGroupCompleter("users"), reserve_space_for_menu=0)

        while True:
            HelpFunctions.listUsers()

            username = session.prompt("User name: ").lower().strip()

            if not username:
                print("Username cannot be empty.")
                continue

            if must_exist and not HelpFunctions.userExists(username):
                print("User does not exist.")
                continue

            if not must_exist and HelpFunctions.userExists(username):
                print("User already exists.")
                continue

            return username

    @staticmethod
    def groupName(must_exist=True):
        from prompt_toolkit import PromptSession
        from ..shell.user_group_completer import UserGroupCompleter

        session = PromptSession(completer=UserGroupCompleter("groups"), reserve_space_for_menu=0)

        while True:
            HelpFunctions.listGroups()

            group_input = session.prompt(
                "Group name(s) (comma separated): "
            ).strip().lower()

            if not group_input:
                return []

            groups = [g.strip() for g in group_input.split(",") if g.strip()]
            valid_groups = []

            for g in groups:
                exists = HelpFunctions.groupExists(g)

                if must_exist and not exists:
                    print(f"Group '{g}' does not exist.")
                    continue

                if not must_exist and exists:
                    print(f"Group '{g}' already exists.")
                    continue

                valid_groups.append(g)

            return valid_groups

    @staticmethod
    def executeCmd(cmd, check=True, capture=False):
        import subprocess

        try:
            result = subprocess.run(
                cmd,
                check=check,
                capture_output=capture,
                text=True
            )
            return result

        except subprocess.CalledProcessError as e:
            print(f"\n[COMMAND FAILED]")
            print(f"Command: {' '.join(cmd)}")
            print(f"Exit Code: {e.returncode}")
            if e.stderr:
                print(f"Error Output: {e.stderr.strip()}")
            return None

        except FileNotFoundError:
            print(f"\n[ERROR] Command not found: {cmd[0]}")
            return None

        except Exception as e:
            print(f"\n[UNEXPECTED ERROR] {e}")
            return None

    @staticmethod
    def folder(base_path=None, must_exist=True):
        from ..shell.foldercompleter import FolderCompleter
        import os
        while True:

            folder = FolderCompleter.folderPrompt(base_path)

            if folder is None:
                return None

            if must_exist and not os.path.isdir(folder):
                print("Folder does not exist.")
                continue

            if not must_exist and os.path.exists(folder):
                print("Folder already exists.")
                continue

            return folder

    @staticmethod
    def preHomeDir(username):
        result = Functions.executeCmd(
            ["getent", "passwd", username],
            capture=True
        )

        if result and result.stdout:
            parts = result.stdout.strip().split(":")
            if len(parts) > 5:
                return (parts[5])

    @staticmethod
    def path(base_path=None, must_exist=True):
        from ..shell.foldercompleter import FolderCompleter
        import os

        while True:

            path = FolderCompleter.folderPrompt(base_path)

            if path is None:
                return None

            if must_exist and not os.path.exists(path):
                print("Path does not exist.")
                continue

            if not must_exist and os.path.exists(path):
                print("Path already exists.")
                continue

            return path

    @staticmethod
    def isSameFilesystem(path1, path2):
        try:
            return os.stat(path1).st_dev == os.stat(path2).st_dev
        except Exception:
            return False

    @staticmethod
    def isLink(path):
        return os.path.islink(path)

class HelpFunctions:

    @staticmethod
    def getUsers():
        result = Functions.executeCmd(
            ["bash", "-c", "getent passwd | awk -F: '$3 >= 1000 {print $1}'"],
            capture=True
        )
        if result and result.stdout:
            return result.stdout.strip().split("\n")
        return []

    @staticmethod
    def listUsers():
        users = HelpFunctions.getUsers()
        if users:
            print("\n".join(users))


    @staticmethod
    def passInfo():
        username = Functions.userName()
        cmd = ["sudo", "chage", "-l", username]

        result = Functions.executeCmd(cmd, capture=True)
        if result and result.stdout:
            print(result.stdout.strip())

    @staticmethod
    def getHomeDir():
        username = Functions.userName()
        result = Functions.executeCmd(
            ["getent", "passwd", username],
            capture=True
        )

        if result and result.stdout:
            parts = result.stdout.strip().split(":")
            if len(parts) > 5:
                print(parts[5])

    @staticmethod
    def userLocked():
        username = Functions.userName()
        cmd = ["sudo", "passwd", "-S", username]

        result = Functions.executeCmd(cmd, capture=True)
        if result and result.stdout:
            print(result.stdout.strip())

    @staticmethod
    def userExpDay():
        username = Functions.userName()
        result = Functions.executeCmd(
            ["sudo", "chage", "-l", username],
            capture=True
        )

        if result and result.stdout:
            for line in result.stdout.splitlines():
                if "Account expires" in line:
                    print(line.strip())

    @staticmethod
    def idUser():
        username = Functions.userName()
        result = Functions.executeCmd(["id", username], capture=True)
        if result and result.stdout:
            print(result.stdout.strip())

    @staticmethod
    def getentUser():
        username = Functions.userName()
        result = Functions.executeCmd(["getent", "passwd", username], capture=True)
        if result and result.stdout:
            print(result.stdout.strip())

    @staticmethod
    def getGroups():
        result = Functions.executeCmd(
            ["bash", "-c", "getent group | awk -F: '$3 >= 1000 || $1 ~ /^(sudo|wheel|docker)$/ {print $1}'"],
            capture=True
        )
        if result and result.stdout:
            return result.stdout.strip().split("\n")
        return []

    @staticmethod
    def listGroups():
        groups = HelpFunctions.getGroups()
        if groups:
            print("\n".join(groups))

    @staticmethod
    def listGroupInfo():
        groupnames = Functions.groupName(must_exist=True)

        if not groupnames:
            print("No valid group selected.")
            return

        for groupname in groupnames:
            cmd = ["getent", "group", groupname]
            result = Functions.executeCmd(cmd, capture=True)

            if result and result.stdout:
                print(result.stdout.strip())

    @staticmethod
    def listUserGroups():
        username = Functions.userName()
        cmd = ["groups", username]

        result = Functions.executeCmd(cmd, capture=True)
        if result and result.stdout:
            print(result.stdout.strip())

    @staticmethod
    def userExists(username):
        result = Functions.executeCmd(
            ["id", username],
            check=False,
            capture=True
        )
        return result is not None and result.returncode == 0

    @staticmethod
    def groupExists(groupname):
        result = Functions.executeCmd(
            ["getent", "group", groupname],
            check=False,
            capture=True
        )
        return result is not None and result.returncode == 0

    @staticmethod
    def uidExists(uid):
        result = Functions.executeCmd(
            ["bash", "-c", f"getent passwd | awk -F: '$3 == {uid}'"],
            check=False,
            capture=True
        )
        return bool(result and result.stdout.strip())

    @staticmethod
    def gidExists(gid):
        result = Functions.executeCmd(
            ["bash", "-c", f"getent group | awk -F: '$3 == {gid}'"],
            check=False,
            capture=True
        )
        return bool(result and result.stdout.strip())

    @staticmethod
    def listAllLinks(directory):
        try:

            links = []

            for root, dirs, files in os.walk(directory):

                for name in files + dirs:

                    full_path = os.path.join(root, name)

                    if os.path.islink(full_path):

                        links.append(full_path)

            return links

        except Exception:
            return []



    @staticmethod
    def printAllLinks():
        directory = Functions.folder(must_exist=True)

        if not directory:
            return

        links = HelpFunctions.listAllLinks(directory)

        if not links:
            print("No links found.")
            return

        print("\nAll symbolic links:\n")

        for link in links:

            try:
                target = os.readlink(link)
                print(f"{link} -> {target}")

            except Exception:
                print(link)
