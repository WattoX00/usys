from functions import Functions

class GroupFunctions():
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
