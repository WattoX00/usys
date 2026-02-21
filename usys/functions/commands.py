from .group_cfg import GroupFunctions
from .user_cfg import UserFunctions
from .functions import HelpFunctions

USER_COMMANDS = {
    "adduser": UserFunctions.userAdd,
    "deluser": UserFunctions.deleteUser,
    "passwd": UserFunctions.userPassword,
    "appendgroup": UserFunctions.appendToGroup,
    "rmfgroup": UserFunctions.removeFromGroup,
    "chname": UserFunctions.changeName,
    "chshell": UserFunctions.changeShell,
    "lockuser": UserFunctions.lockUser,
    "unlockuser": UserFunctions.unlockUser,
    "setexp": UserFunctions.setExp,
    "rmexp": UserFunctions.removeExp,
    "chuid": UserFunctions.changeUserId,
    "listusers": HelpFunctions.listUsers,
    "listusergroups": HelpFunctions.listUserGroups,
    "homedir": HelpFunctions.getHomeDir,
    "passinfo": HelpFunctions.passInfo,
    "userlocked": HelpFunctions.userLocked,
    "userexpday": HelpFunctions.userExpDay,
    "help": UserFunctions.helpText,
    "helpf": UserFunctions.fullHelp,
    "quit": quit,
}

USER_ALIASES = {
    "au": "adduser",
    "du": "deluser",
    "pw": "passwd",
    "ag": "appendgroup",
    "ar": "rmfgroup",
    "cn": "chname",
    "cs": "chshell",
    "luu": "lockuser",
    "ulu": "unlockuser",
    "se": "setexp",
    "re": "rmexp",
    "uid": "chuid",
    "lu": "listusers",
    "lug": "listusergroups",
    "hd": "homedir",
    "pi": "passinfo",
    "ul": "userlocked",
    "ued": "userexpday",
    "h": "help",
    "hf": "helpf",
    "q": "quit",
}

GROUP_COMMANDS = {
    "addgroup": GroupFunctions.groupAdd,
    "rmgroup": GroupFunctions.groupRemove,
    "chgroup": GroupFunctions.chGroupName,
    "delgroup": GroupFunctions.groupDel,
    "listgroups": HelpFunctions.listGroups,
    "chgid": GroupFunctions.changeGroupId,
    "groupinfo": HelpFunctions.listGroupInfo,
    "help": GroupFunctions.helpText,
    "helpf": UserFunctions.fullHelp,
    "quit": quit,
}

GROUP_ALIASES = {
    "ga": "addgroup",
    "gr": "rmgroup",
    "cg": "chgroup",
    "gd": "delgroup",
    "lg": "listgroups",
    "gi": "groupinfo",
    "gid": "chgid",
    "h": "help",
    "hf": "helpf",
    "q": "quit",
}

def root_help():
    print("""
    Command     Alias   Description

    user        (u)     User management
    group       (g)     Group management
    help        (h)     Show this help menu
    exit        (q)     Exit the program
    """)

def helpFull():
    print("""
    USYS - linux user manager :)


    USER COMMANDS

    adduser     (au)  - Create a new user account
    deluser     (du)  - Remove an existing user account
    passwd      (pw)  - Change a user's password
    chname      (cn)  - Modify an existing username
    chshell     (cs)  - Change the user's default shell
    listuser    (lu)  - Display all registered users
    homedir     (hd)  - Show the user's home directory path

    GROUP COMMANDS

    addgroup    (ga)  - Create a new group
    delgroup    (gd)  - Delete an existing group
    appendgroup (ag)  - Add a user to an existing group
    listgroups  (lg)  - Display all groups
    groupinfo   (gi)  - Show detailed information about a group

    GENERAL

    quit        (q)   - Exit the program
    """)

# todo :

# add flags

# add ssh
# add samba
# add github ssh setup
# add apache setup
# add errorhandling ; user permission managment ; foldere permissions
