from group_cfg import GroupFunctions
from user_cfg import UserFunctions
from functions import HelpFunctions

USER_COMMANDS = {
    "adduser": UserFunctions.userAdd,
    "deluser": UserFunctions.deleteUser,
    "passwd": UserFunctions.userPassword,
    "appendgroup": UserFunctions.appendToGroup,
    "chname": UserFunctions.changeName,
    "chshell": UserFunctions.changeShell,
    "listusers": HelpFunctions.listUsers,
    "homedir": HelpFunctions.getHomeDir,
    "help": UserFunctions.helpText,
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
    "h": "help",
}

GROUP_COMMANDS = {
    "addgroup": GroupFunctions.groupAdd,
    "rmgroup": GroupFunctions.groupRemove,
    "chgroup": GroupFunctions.chGroupName,
    "delgroup": GroupFunctions.groupDel,
    "listgroups": HelpFunctions.listGroups,
    "groupinfo": HelpFunctions.listGroupInfo,
    "help": GroupFunctions.helpText,
}

GROUP_ALIASES = {
    "ga": "addgroup",
    "gr": "rmgroup",
    "cg": "chgroup",
    "gd": "delgroup",
    "lg": "listgroups",
    "gi": "groupinfo",
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

