from functions import Functions, HelpFunctions
from group_cfg import GroupFunctions
from user_cfg import UserFunctions

# --- USER COMMANDS ---
USER_COMMANDS = {
    "adduser": UserFunctions.userAdd,
    "deluser": UserFunctions.deleteUser,
    "passwd": UserFunctions.userPassword,
    "appendgroup": UserFunctions.appendToGroup,
    "chname": UserFunctions.changeName,
    "chshell": UserFunctions.changeShell,
    "listusers": HelpFunctions.listUsers,
}

USER_ALIASES = {
    "au": "adduser",
    "du": "deluser",
    "pw": "passwd",
    "ag": "appendgroup",
    "cn": "chname",
    "cs": "chshell",
    "lu": "listusers",
}

# --- GROUP COMMANDS ---
GROUP_COMMANDS = {
    "addgroup": GroupFunctions.groupAdd,
    "rmgroup": GroupFunctions.groupRemove,
    "chgroup": GroupFunctions.chGroupName,
    "delgroup": GroupFunctions.groupDel,
    "listgroups": HelpFunctions.listGroups,
}

GROUP_ALIASES = {
    "ga": "addgroup",
    "gr": "rmgroup",
    "cg": "chgroup",
    "gd": "delgroup",
    "lg": "listgroups"
}


# --- MODE SWITCH TABLE ---
COMMAND_SETS = {
    "user": (USER_COMMANDS, USER_ALIASES),
    "group": (GROUP_COMMANDS, GROUP_ALIASES),
}

# todo : 
# dividee the app into segments

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

