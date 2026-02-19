class Functions():

    def userName():
        HelpFunctions.listUsers()
        username = str(input('User name: ')).lower().strip()
        return username

    def groupName():
        HelpFunctions.listGroups()
        groupname = str(input('Group name: ')).lower().strip()

    def executeCmd(cmd, check=True, capture=False):
        import subprocess
        return subprocess.run(cmd, check=check, capture_output=capture, text=True)

class HelpFunctions():

    #listings
    def listUsers():
        result = Functions.executeCmd(["bash", "-c", "getent passwd | awk -F: '$3 >= 1000 {print $1}'"], capture=True)
        print(result.stdout)

    def listGroups():
        result = Functions.executeCmd(["bash", "-c", "getent group | awk -F: '$3 >= 1000 || $1 ~ /^(sudo|wheel|docker)$/ {print $1}'"], capture=True)
        print(result.stdout)

    def getHomeDir():
        username = Functions.userName()
        result = Functions.executeCmd(["getent", "passwd", username], capture=True)

        home = result.stdout.split(":")[5]
        print(home)

    def listGroupInfo():
        groupname = Functions.groupName()
        cmd = ["getent", "group", groupname[0]]

        print(Functions.executeCmd(cmd, capture=True).stdout)

    def listUserGroups():
        username = Functions.userName()
        cmd = ["groups", username]

        print(Functions.executeCmd(cmd, capture=True).stdout)

    # Helpers
    def groupName():
        Functions.listGroups()
        groupname = str(input('Group name separated by space: ')).lower().strip()
        return groupname.split(' ')

    # HELP function :)
    def helpText():
        print("""
        Commands (alias):
        adduser      (au)   deluser      (du)
        passwd       (pw)   appendgroup  (ag)
        chname       (cn)   chshell      (cs)
        addgroup     (ga)   delgroup     (gd)
        listuser     (lu)   listgroups   (lg)
        groupinfo    (gi)   homedir      (hd)
        """)
