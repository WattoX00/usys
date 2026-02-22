from .functions import Functions, HelpFunctions

class GroupFunctions:

    @staticmethod
    def groupAdd():
        groupnames = Functions.groupName(must_exist=False)

        if not groupnames:
            print("No valid group names provided.")
            return

        for groupname in groupnames:
            cmd = ["sudo", "groupadd", groupname]
            result = Functions.executeCmd(cmd)

            if result:
                print(f"Group '{groupname}' created successfully.")

    @staticmethod
    def groupRemove():
        username = Functions.userName()
        groupnames = Functions.groupName(must_exist=True)

        if not groupnames:
            print("No valid groups selected.")
            return

        for groupname in groupnames:
            cmd = ["sudo", "gpasswd", "-d", username, groupname]
            result = Functions.executeCmd(cmd)

            if result:
                print(f"Removed '{username}' from group '{groupname}'.")

    @staticmethod
    def chGroupName():
        groupnames = Functions.groupName(must_exist=True)

        if not groupnames:
            print("No valid group selected.")
            return

        groupname = groupnames[0]

        newgroup = input("New name of the group: ").strip().lower()

        if not newgroup:
            print("New group name cannot be empty.")
            return

        if HelpFunctions.groupExists(newgroup):
            print("Group with that name already exists.")
            return

        cmd = ["sudo", "groupmod", "-n", newgroup, groupname]
        result = Functions.executeCmd(cmd)

        if result:
            print(f"Group '{groupname}' renamed to '{newgroup}'.")

    @staticmethod
    def groupDel():
        groupnames = Functions.groupName(must_exist=True)

        if not groupnames:
            print("No valid group selected.")
            return

        for groupname in groupnames:
            cmd = ["sudo", "groupdel", groupname]
            result = Functions.executeCmd(cmd)

            if result:
                print(f"Group '{groupname}' deleted.")

    @staticmethod
    def changeGroupId():
        groupnames = Functions.groupName(must_exist=True)

        if not groupnames:
            print("No valid group selected.")
            return

        groupname = groupnames[0]

        try:
            newid = int(input("New Group Id: ").strip())
        except ValueError:
            print("Invalid GID. Must be a number.")
            return

        if HelpFunctions.gidExists(newid):
            print("That GID is already in use.")
            return

        cmd = ["sudo", "groupmod", "-g", str(newid), groupname]
        result = Functions.executeCmd(cmd)

        if result:
            print(f"GID of '{groupname}' changed to {newid}.")

    # Help text
    def helpText():
        print("""
    Command        Alias   Description

    addgroup       (ga)    Create a new group
    delgroup       (gd)    Delete an existing group
    listgroups     (lg)    List all groups
    groupinfo      (gi)    Show detailed group information

    help           (h)     Show help menu
    helpf          (hf)    Show full help menu
    quit           (q)     Quit the program
    """)

    def fullHelp():
        print("""
               GROUP MANAGEMENT
    addgroup        (ga)    Create a new group
    rmgroup         (gr)    Remove group (soft removal)
    delgroup        (gd)    Delete group permanently
    chgroup         (cg)    Change group name
    chgid           (gid)   Change group ID

            INFORMATION & LISTING
    listgroups      (lg)    List all groups
    groupinfo       (gi)    Show detailed group information

                 HELP & EXIT
    help            (h)     Show help menu
    helpf           (hf)    Show full help menu
    quit            (q)     Quit the program
    """)
