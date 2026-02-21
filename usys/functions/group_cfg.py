from .functions import Functions

class GroupFunctions():
    # GROUPS
 
    def groupAdd():
        groupname = Functions.groupName()
        cmd = ["sudo", "groupadd", groupname]

        Functions.executeCmd(cmd)

    def groupRemove():
        username = Functions.userName()
        groupName = Functions.groupName()

        groups = ','.join(groupName)
        cmd = ["sudo", "usermod", "-rG", groups, username]

        Functions.executeCmd(cmd)

    def chGroupName():
        groupname = Functions.groupName()
        newgroup = str(input('New name of the group: '))
        cmd = ["sudo", "groupmod", "-n", newgroup, groupname]

        Functions.executeCmd(cmd)

    def groupDel():
        groupname = Functions.groupName()
        cmd = ["sudo", "groupdel", groupname]

        Functions.executeCmd(cmd)

    def changeGroupId():
        groupname = Functions.groupName()
        newid = int(input('New Group Id: '))
        cmd = ["sudo", "groupmod", "-g", newid, groupname]

        Functions.executeCmd(cmd)

    # Help text
    def helpText():
        print("""
    Command       Alias   Description

    addgroup      (ga)    Create a new group
    delgroup      (gd)    Delete an existing group
    listgroups    (lg)    List all groups
    groupinfo     (gi)    Show detailed group information
    help          (h)     Show help menu
    quit          (q)     Quit the program
    """)

    def fulHelp():
        print("""
    Command       Alias   Description

    addgroup      (ga)    Create a new group
    rmgroup       (gr)    Remove group
    chgroup       (cg)    Change group name
    delgroup      (gd)    Delete group permanently
    listgroups    (lg)    List all groups
    groupinfo     (gi)    Show detailed group information
    chgid         (gid)   Change group ID
    help          (h)     Show help menu
    quit          (q)     Quit the program
    """)
