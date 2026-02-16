# add errorhandling samba setup ; user permission managment ; foldere permissions
class Functions():

    # add a user
    def userAdd():
        newUserName = Functions.userName()

        cmd = ["sudo", "useradd"]

        # Home directory
        homeQ = input(f'Do you want to add home directory [home/{newUserName}] (Y/n) ').lower()
        if homeQ in ("y", "yes", ""):
            cmd.append("-m")

        # Groups
        groupQ = input(f'Do you want to add ({newUserName}) to a group (Y/n) ').lower()
        if groupQ in ("y", "yes", ""):
            Functions.listGroups()
            groups = Functions.groupName()

            if len(groups) == 1:
                cmd += ["-g", groups[0]]

            if len(groups) > 1:
                cmd += ["-G", ",".join(groups[1:])]

        cmd.append(newUserName)

        Functions.executeCmd(cmd)

    # remove user
    def deleteUser():
        username = Functions.userName()

        cmd = ["sudo", "userdel", "-r", username]

        Functions.executeCmd(cmd)

    # Add/change password
    def userPassword():
        username = Functions.userName()
        cmd = ["sudo", "passwd", username]
        Functions.executeCmd(cmd)
 
    # Append to Groups
    def appendToGroup():
        username = Functions.userName()
        groupName = Functions.groupName()

        groups = ','.join(groupName)
        cmd = ["sudo", "usermod", "-aG", groups, username]

        Functions.executeCmd(cmd)

    # Change name
    def changeName():
        old = Functions.userName()
        new = str(input('New name: '))
        cmd = ["sudo", "usermod", "-l", new, old]

        Functions.executeCmd(cmd)
 
    # Change shell
    def changeShell():
        username = Functions.userName()
        shellname = str(input('Change shell full path (/bin/bash): '))
        cmd = ["sudo", "usermod", "-s", shellname, username]

        Functions.executeCmd(cmd)
    # GROUPS

    # sudo groupadd <groupname>
    def groupAdd():
        groupname = Functions.groupName()
        cmd = ["sudo", "groupadd", groupname]

        Functions.executeCmd(cmd)

    def groupDel():
        username = Functions.userName()
        groupName = Functions.groupName()

        groups = ','.join(groupName)
        cmd = ["sudo", "usermod", "-rG", groups, username]

        Functions.executeCmd(cmd)

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

    def userName():
        Functions.listUsers()
        username = str(input('User name: ')).lower().strip()
        return username

    def executeCmd(cmd, check=True, capture=False):
        import subprocess
        return subprocess.run(cmd, check=check, capture_output=capture, text=True)

    # HELP function :)
    def helpText():
        print("""
    USER MANAGEMENT CLI – HELP

    COMMANDS
    --------

    adduser (au)
        Create a new user.

    deluser (du)
        Delete an existing user.

    passwd (pw)
        Change a user's password.

    appendgroup (ag)
        Add a user to a group.

    chname (cn)
        Change the username.

    chshell (cs)
        Change the user's shell.

    addgroup (ga)
        Create a new group.

    delgroup (gd)
        Delete an existing group.

    listuser (lu)
        List all users.

    listgroups (lg)
        List all groups.

    groupinfo (gi)
        Show detailed information about a group.

    homedir (hd)
        Show the home directory of a user.

       """)

