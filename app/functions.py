import subprocess

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
        listGroups()
        groupName = input('Primary group first, then secondary groups separated by space: ').lower()
        groups = groupName.split()

        if len(groups) >= 1:
            cmd += ["-g", groups[0]]

        if len(groups) > 1:
            cmd += ["-G", ",".join(groups[1:])]

    cmd.append(newUserName)

    subprocess.run(cmd)

def listGroups():
    subprocess.run([
        "bash",
        "-c",
        "getent group | awk -F: '$3 >= 1000 || $1 ~ /^(sudo|wheel|docker)$/ {print $1}'"
    ])

# userAdd()

def deleteUser():
    name = str(input(''))

    cmd = ["sudo", "userdel", "-r", name]
    subprocess.run(cmd)
deleteUser()
