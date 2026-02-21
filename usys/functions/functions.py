class Functions():

    def userName():
        HelpFunctions.listUsers()
        username = str(input('User name: ')).lower().strip()
        return username

    def groupName():
        HelpFunctions.listGroups()
        groupname = str(input('Group name: ')).lower().strip()
        return groupname

    def executeCmd(cmd, check=True, capture=False):
        import subprocess
        return subprocess.run(cmd, check=check, capture_output=capture, text=True)

class HelpFunctions():

    #listings
    def listUsers():
        result = Functions.executeCmd(["bash", "-c", "getent passwd | awk -F: '$3 >= 1000 {print $1}'"], capture=True)
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

    def listGroups():
        result = Functions.executeCmd(["bash", "-c", "getent group | awk -F: '$3 >= 1000 || $1 ~ /^(sudo|wheel|docker)$/ {print $1}'"], capture=True)
        print(result.stdout)


    def listGroupInfo():
        groupname = Functions.groupName()
        cmd = ["getent", "group", groupname]

        print(Functions.executeCmd(cmd, capture=True).stdout)

    def listUserGroups():
        username = Functions.userName()
        cmd = ["groups", username]

        print(Functions.executeCmd(cmd, capture=True).stdout)

