import subprocess

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

        subprocess.run(cmd)

    # remove user
    def deleteUser():
        Functions.listUsers()
        username = str(input('Remove user [name]: '))
        cmd = ["sudo", "userdel"]
        if Functions.getHomeDir(username):
            cmd.append("-r")
        cmd.append(username)
        subprocess.run(cmd)

    # Add/change password
    def userPassword():
        Functions.listUsers()
        username = str(input('Change password for user [name]: '))
        cmd = ["sudo", "passwd", username]
        subprocess.run(cmd)
 
    # Append to Groups
    def appendToGroup():
        Functions.listUsers()
        username = str(input('USERNAME: '))
        Functions.listGroups()
        groupName = input('Groups separated by space: ').lower()
        group = groupName.split(' ')
        groups = ','.join(group)
        cmd = ["sudo", "usermod", "-aG", groups, username]
        subprocess.run(cmd)

    # Change name
    def changeName():
        Functions.listUsers()
        old = str(input('User to change name [name]: '))
        new = str(input('New name: '))
        cmd = ["sudo", "usermod", "-l", new, old]
        subprocess.run(cmd)
 
    # Change shell
    def changeShell():
        Functions.listUsers()
        username = str(input('USERNAME: '))
        shellname = str(input('Change shell full path (/bin/bash): '))
        cmd = ["sudo", "usermod", "-s", shellname]
        subprocess.run(cmd)
    # GROUPS

    # sudo groupadd <groupname>
    def groupAdd():
        groupname = str(input('New group [name]: '))
        cmd = ["sudo", "groupadd", groupname]
        subprocess.run(cmd)

    #listings
    def listUsers():
        subprocess.run(["bash", "-c", "getent passwd | awk -F: '$3 >= 1000 {print $1}'"])

    def listGroups():
        subprocess.run(["bash", "-c", "getent group | awk -F: '$3 >= 1000 || $1 ~ /^(sudo|wheel|docker)$/ {print $1}'"])

    def getHomeDir(username):
        result = subprocess.run(
            ["getent", "passwd", username],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            home = result.stdout.split(":")[5]
            return(home)

    def listGroupInfo():
        groupname = Functions.groupName()
        cmd = ["getent", "group", groupname[0]]
        subprocess.run(cmd)

    def listUserGroups():
        username = Functions.userName()
        cmd = ["groups", username]
        subprocess.run(cmd)

    # Helpers
    def groupName():
        Functions.listGroups()
        groupname = str(input('Group name separated by space: ')).lower().strip()
        return groupname.split(' ')

    def userName():
        Functions.listUsers()
        username = str(input('User name: ')).lower().strip()
        return username

