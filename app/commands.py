from functions import Functions

COMMANDS = {
    "adduser": Functions.userAdd,
    "deluser": Functions.deleteUser,
    "passwd": Functions.userPassword,
    "appendgroup": Functions.appendToGroup,
    "chname": Functions.changeName,
    "chshell": Functions.changeShell,
    "addgroup": Functions.groupAdd,
    "delgroup": Functions.groupDel,
    "listuser": Functions.listUsers,
    "listgroups": Functions.listGroups,
    "groupinfo": Functions.listGroupInfo,
    "homedir": Functions.getHomeDir,
    "help": Functions.helpText,
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

