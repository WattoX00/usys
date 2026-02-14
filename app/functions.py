import subprocess

class Functions():

    # add a user

    def userAdd():
        newUserName = input('New User Name: ').strip()

        cmd = ["sudo", "useradd"]

        # Home directory
        homeQ = input(f'Do you want to add home directory [home/{newUserName}] (Y/n) ').lower()
        if homeQ in ("y", "yes", ""):
            cmd.append("-m")

        # Groups
        groupQ = input(f'Do you want to add ({newUserName}) to a group (Y/n) ').lower()
        if groupQ in ("y", "yes", ""):
            Functions.listGroups()
            groupName = input('Primary group first, then secondary groups separated by space: ').lower()
            groups = groupName.split()

            if len(groups) >= 1:
                cmd += ["-g", groups[0]]

            if len(groups) > 1:
                cmd += ["-G", ",".join(groups[1:])]

        cmd.append(newUserName)

        subprocess.run(cmd)

    # remove user with home dir

    def deleteUser():
        username = str(input('Remove user [name]: '))
        cmd = ["sudo", "userdel"]
        if Functions.getHomeDir(username):
            cmd.append("-r")
        cmd.append(username)
        subprocess.run(cmd)

    def userPassword():
        username = str(input('Change password for user [name]: '))
        cmd = ["sudo", "passwd", username]
        subprocess.run(cmd)
    
    def appendToGroup():
        cmd = ["sudo", "-aG", group]
    
    def changeName():
        cmd = ["sudo", "usermod", "-l", new, old]

    def changeShell():
        cmd = ["sudo", "usermod", "-s", shellname]
    # append to group (-aG group name)
    # change name (usermod -l new old)
    # change shell (-s shell name)

    # GROUPS
    # sudo groupadd <groupname>
    # change name groupmod -n <newname> <oldname>
    # delete user from group gpasswd -d <user> <group>
    # delete group sudo groupdel <groupname>

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


    # READ MORE GROUP stuff
    # getent group <groupname>
    # groups <username>


