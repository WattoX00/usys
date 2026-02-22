class Functions():

    @staticmethod
    def userName(must_exist=True):
        while True:
            HelpFunctions.listUsers()
            username = input('User name: ').lower().strip()

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
        HelpFunctions.listGroups()
        group_input = input('Group name(s) (comma separated): ').strip().lower()

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

class HelpFunctions():

    #listings
    def listUsers():
        result = Functions.executeCmd(["bash", "-c", "getent passwd | awk -F: '$3 >= 1000 {print $1}'"], capture=True)
        if result and result.stdout:
            print(result.stdout)

    def passInfo():
        username = Functions.userName()
        cmd = ["chage", "-l", username]

        print(Functions.executeCmd(cmd, capture=True).stdout)

    def getHomeDir():
        username = Functions.userName()
        result = Functions.executeCmd(["getent", "passwd", username], capture=True)

        home = result.stdout.split(":")[5]
        print(home)
 
    def userLocked():
        username = Functions.userName()
        cmd = ["passwd", "-S", username]

        print(Functions.executeCmd(cmd, capture=True).stdout)

    def userExpDay():
        username = Functions.userName()
        result = Functions.executeCmd(["bash", "-c", f"chage -l {username} | grep 'Account expires'"], capture=True)
        if result and result.stdout:
            print(result.stdout)

    def listGroups():
        result = Functions.executeCmd(["bash", "-c", "getent group | awk -F: '$3 >= 1000 || $1 ~ /^(sudo|wheel|docker)$/ {print $1}'"], capture=True)
        if result and result.stdout:
            print(result.stdout)

    def listGroupInfo():
        groupname = Functions.groupName()
        cmd = ["getent", "group", groupname]

        print(Functions.executeCmd(cmd, capture=True).stdout)

    def listUserGroups():
        username = Functions.userName()
        cmd = ["groups", username]

        print(Functions.executeCmd(cmd, capture=True).stdout)
 
    @staticmethod
    def userExists(username):
        result = Functions.executeCmd(
            ["id", username],
            check=False,
            capture=True
        )
        return result.returncode == 0

    @staticmethod
    def groupExists(groupname):
        result = Functions.executeCmd(
            ["getent", "group", groupname],
            check=False,
            capture=True
        )
        return result.returncode == 0

    @staticmethod
    def uidExists(uid):
        result = Functions.executeCmd(
            ["getent", "passwd", str(uid)],
            check=False,
            capture=True
        )
        return bool(result.stdout.strip())
