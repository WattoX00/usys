from .functions import Functions

class GroupFunctions():
    # GROUPS
 
    def groupAdd():
        groupnames = Functions.groupName()

        if not groupnames:
            print("No valid group names provided.")
            return

        for groupname in groupnames:
            cmd = ["sudo", "groupadd", groupname]
            result = Functions.executeCmd(cmd)

            if result:
                print(f"Group '{groupname}' created successfully.")

    def groupRemove():
        username = Functions.userName()
        groupnames = Functions.groupName()

        if not groupnames:
            print("No valid groups selected.")
            return

        groups = ",".join(groupnames)

        cmd = ["sudo", "usermod", "-rG", groups, username]
        result = Functions.executeCmd(cmd)

    if result:
        print(f"Removed {groups} from {username}.")

    def chGroupName():
        groupnames = Functions.groupName()

        if not groupnames:
            print("No valid group selected.")
            return

        groupname = groupnames[0]  # Only rename one group

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

    def groupDel():
        groupnames = Functions.groupName()

        if not groupnames:
            print("No valid group selected.")
            return

        for groupname in groupnames:
            cmd = ["sudo", "groupdel", groupname]
            result = Functions.executeCmd(cmd)

            if result:
                print(f"Group '{groupname}' deleted.")

    def changeGroupId():
        groupnames = Functions.groupName()

        if not groupnames:
            print("No valid group selected.")
            return

        groupname = groupnames[0]

        try:
            newid = int(input("New Group Id: ").strip())
        except ValueError:
            print("Invalid GID. Must be a number.")
            return

        if HelpFunctions.uidExists(newid):
            print("That GID is already in use.")
            return

        cmd = ["sudo", "groupmod", "-g", str(newid), groupname]
        result = Functions.executeCmd(cmd)

        if result:
            print(f"GID of '{groupname}' changed to {newid}.")

    # Help text
    def helpText():
        print("""
    Command       Alias   Description

    addgroup      (ga)    Create a new group
    delgroup      (gd)    Delete an existing group
    listgroups    (lg)    List all groups
    groupinfo     (gi)    Show detailed group information
    help          (h)     Show help menu
    helpf         (hf)    Show full help menu
    exit          (e)     Go back to root
    quit          (q)     Quit the program
    """)

    def fullHelp():
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
    helpf         (hf)    Show full help menu
    exit          (e)     Go back to root
    quit          (q)     Quit the program
    """)
