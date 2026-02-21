from .functions import Functions, HelpFunctions
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

    def removeFromGroup():
        username = Functions.userName()
        groupname = Functions.groupName()
        cmd = ["sudo", "gpasswd", username, groupname]

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

    def lockUser():
        username = Functions.userName()
        cmd = ["sudo", "usermod", "-L", username]

        Functions.executeCmd(cmd)

    def unlockUser():
        username = Functions.userName()
        cmd = ["sudo", "usermod", "-U", username]

        Functions.executeCmd(cmd)

    def setExp():
        username = Functions.userName()
        date = str(input('Exp day')) # YYYY-MM-DD
        cmd = ["sudo", "chage", "-E", date, username]

        Functions.executeCmd(cmd)

    def removeExp():
        username = Functions.userName()
        cmd = ["sudo", "chage", "-1", username]

        Functions.executeCmd(cmd)

    def changeUserId():
        usermod -u new_uid username
        username = Functions.userName()
        newid = int(input('New UID: '))
        cmd = ["sudo", "usermod", "-u", newid, username]

        Functions.executeCmd(cmd)

    # help text
    def helpText():
        print("""
    Command     Alias   Description

    adduser     (au)    Create a new user
    deluser     (du)    Delete an existing user
    passwd      (pw)    Change user password
    chname      (cn)    Change username
    chshell     (cs)    Change user shell
    listusers   (lu)    List all users
    homedir     (hd)    View home directory
    help        (h)     Show help menu
    quit        (q)     Quit the program
    """)

    def fullHelp():
        print("""
    Command           Alias   Description

    adduser           (au)    Create a new user
    deluser           (du)    Delete an existing user
    passwd            (pw)    Change user password
    appendgroup       (ag)    Add user to an existing group
    rmfgroup          (ar)    Remove user from a group
    chname            (cn)    Change username
    chshell           (cs)    Change user shell
    lockuser          (luu)   Lock user account
    unlockuser        (ulu)   Unlock user account
    setexp            (se)    Set account expiration date
    rmexp             (re)    Remove account expiration
    chuid             (uid)   Change user ID
    listusers         (lu)    List all users
    listusergroups    (lug)   List groups of a user
    homedir           (hd)    View home directory
    passinfo          (pi)    Show password information
    userlocked        (ul)    Check if user is locked
    userexpday        (ued)   Show user expiration day
    help              (h)     Show help menu
    quit              (q)     Quit the program
    """)
