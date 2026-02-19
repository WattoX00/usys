from shell import run_shell
from functions import HelpFunctions
from group_cfg import GroupFunctions
from user_cfg import UserFunctions

USER_COMMANDS = {
    "adduser": UserFunctions.userAdd,
    "deluser": UserFunctions.deleteUser,
    "passwd": UserFunctions.userPassword,
    "appendgroup": UserFunctions.appendToGroup,
    "chname": UserFunctions.changeName,
    "chshell": UserFunctions.changeShell,
    "listusers": HelpFunctions.listUsers,
    "homedir": HelpFunctions.getHomeDir,
}

USER_ALIASES = {
    "au": "adduser",
    "du": "deluser",
    "pw": "passwd",
    "ag": "appendgroup",
    "cn": "chname",
    "cs": "chshell",
    "lu": "listusers",
    "hd": "homedir",
}

GROUP_COMMANDS = {
    "addgroup": GroupFunctions.groupAdd,
    "rmgroup": GroupFunctions.groupRemove,
    "chgroup": GroupFunctions.chGroupName,
    "delgroup": GroupFunctions.groupDel,
    "listgroups": HelpFunctions.listGroups,
    "groupinfo": HelpFunctions.listGroupInfo,
}

GROUP_ALIASES = {
    "ga": "addgroup",
    "gr": "rmgroup",
    "cg": "chgroup",
    "gd": "delgroup",
    "lg": "listgroups",
    "gi": "groupinfo",
}

COMMAND_SETS = {
    "user": (USER_COMMANDS, USER_ALIASES),
    "group": (GROUP_COMMANDS, GROUP_ALIASES),
}

ROOT_COMMANDS = {
    "user": lambda: run_shell("user ~ $ ", *COMMAND_SETS["user"]),
    "group": lambda: run_shell("group ~ $ ", *COMMAND_SETS["group"]),
    "help": HelpFunctions.helpText,
}

ROOT_ALIASES = {
    "h": "help",
}


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

