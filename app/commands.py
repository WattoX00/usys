from functions import Functions
from group_cfg import GroupFunctions
from user_cfg import UserFunctions
from help_cfg import HelpFunctions
COMMANDS = {
    # user
    "adduser": UserFunctions.userAdd,
    "deluser": UserFunctions.deleteUser,
    "passwd": UserFunctions.userPassword,
    "appendgroup": UserFunctions.appendToGroup,
    "chname": UserFunctions.changeName,
    "chshell": UserFunctions.changeShell,
    # group
    "addgroup": GroupFunctions.groupAdd,
    "delgroup": GroupFunctions.groupDel,
    #list
    "listuser": HelpFunctions.listUsers,
    "listgroups": HelpFunctions.listGroups,
    "groupinfo": HelpFunctions.listGroupInfo,
    "homedir": HelpFunctions.getHomeDir,
    "help": HelpFunctions.helpText,
}

ALIASES = {
    "au": "adduser",
    "du": "deluser",
    "pw": "passwd",
    "ag": "appendgroup",
    "cn": "chname",
    "cs": "chshell",
    "ga": "addgroup",
    "gd": "delgroup",
    "lu": "listuser",
    "lg": "listgroups",
    "gi": "groupinfo",
    "hd": "homedir",
    "h": "help"
}

# todo : 
# dividee the app into segments

# lock/unlock user: usermod -L username ; usermod -U username

# set expire: expireuser (eu) ; setexpiry  (se)

# passinfo (pi) ; setpasspolicy (sp)

# addusertogroup (aug) ; removeusergroup  (rug) ; setgroups (sg)

# chuid (cuid) ; chgid (cgid)

# cloneuser (cu)

# group:

# chgroupname (cgn)


# add flags

