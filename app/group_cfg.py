from functions import Functions

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

    def helpText():
        print("""
    Command       Alias   Description

    appendgroup   (ag)    Add user to an existing group
    addgroup      (ga)    Create a new group
    delgroup      (gd)    Delete an existing group
    listgroups    (lg)    List all groups
    groupinfo     (gi)    Show detailed group information
    """)
