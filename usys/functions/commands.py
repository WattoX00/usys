from .group_cfg import GroupFunctions
from .user_cfg import UserFunctions
from .functions import HelpFunctions

USER_COMMANDS = {
    "adduser": UserFunctions.userAdd,
    "deluser": UserFunctions.deleteUser,
    "passwd": UserFunctions.userPassword,
    "appendgroup": UserFunctions.appendToGroup,
    "chname": UserFunctions.changeName,
    "chshell": UserFunctions.changeShell,
    "listusers": HelpFunctions.listUsers,
    "listusergroups": HelpFunctions.listUserGroups,
    "homedir": HelpFunctions.getHomeDir,
    "passinfo": HelpFunctions.passInfo,
    "help": UserFunctions.helpText,
    "quit": quit,
}

USER_ALIASES = {
    "au": "adduser",
    "du": "deluser",
    "pw": "passwd",
    "ag": "appendgroup",
    "cn": "chname",
    "cs": "chshell",
    "lu": "listusers",
    "lug": "listusergroups",
    "hd": "homedir",
    "pi": "passinfo",
    "h": "help",
    "q": "quit",
}

GROUP_COMMANDS = {
    "addgroup": GroupFunctions.groupAdd,
    "rmgroup": GroupFunctions.groupRemove,
    "chgroup": GroupFunctions.chGroupName,
    "delgroup": GroupFunctions.groupDel,
    "listgroups": HelpFunctions.listGroups,
    "groupinfo": HelpFunctions.listGroupInfo,
    "help": GroupFunctions.helpText,
    "quit": quit,
}

GROUP_ALIASES = {
    "ga": "addgroup",
    "gr": "rmgroup",
    "cg": "chgroup",
    "gd": "delgroup",
    "lg": "listgroups",
    "gi": "groupinfo",
    "h": "help",
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

# lock/unlock user: usermod -L username ; usermod -U username

# set expire: expireuser (eu) ; setexpiry  (se)

# passinfo (pi) ; setpasspolicy (sp)

# addusertogroup (aug) ; removeusergroup  (rug) ; setgroups (sg)

# chuid (cuid) ; chgid (cgid)

# cloneuser (cu)

# add flags

# add ssh
# add samba
# add github ssh setup
# add apache setup
# add errorhandling ; user permission managment ; foldere permissions
