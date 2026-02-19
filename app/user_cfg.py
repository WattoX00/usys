from functions import Functions, HelpFunctions
class UserFunctions():

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
            HelpFunctions.listGroups()
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
