from .functions import HelpFunctions
from .group_cfg import GroupFunctions
from .user_cfg import UserFunctions
from .ssh_cfg import SSHFunctions
from .samba_cfg import SambaFunctions

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
    "iduser": HelpFunctions.idUser,
    "getentuser": HelpFunctions.getentUser,
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
    "idu": "iduser",
    "gu": "getentuser",
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
    "helpf": GroupFunctions.fullHelp,
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

SSH_COMMANDS = {
    "install": SSHFunctions.installOpenSSH,
    "enable": SSHFunctions.enableService,
    "genkey": SSHFunctions.generateKey,
    "listkeys": SSHFunctions.listKeys,
    "github": SSHFunctions.setupGithubSSH,
    "test": SSHFunctions.testConnection,
    "help": SSHFunctions.helptext,
    "setup": SSHFunctions.setup,
    "quit": quit,
}

SSH_ALIASES = {
    "i": "install",
    "e": "enable",
    "gk": "genkey",
    "lk": "listkeys",
    "gh": "github",
    "t": "test",
    "h": "help",
    "s": "setup",
    "q": "quit",
}

SAMBA_COMMANDS = {
    "install": SambaFunctions.installSamba,
    "start": SambaFunctions.startSamba,
    "stop": SambaFunctions.stopSamba,
    "enable": SambaFunctions.enableSamba,
    "disable": SambaFunctions.disableSamba,
    "restart": SambaFunctions.restartSamba,
    "status": SambaFunctions.sambaStatus,
    "adduser": SambaFunctions.addSambaUser,
    "removeuser": SambaFunctions.removeSambaUser,
    "enableuser": SambaFunctions.enableSambaUser,
    "disableuser": SambaFunctions.disableSambaUser,
    "mkshare": SambaFunctions.createShareFolder,
    "rmshare": SambaFunctions.removeShareFolder,
    "owner": SambaFunctions.setFolderOwner,
    "chmod": SambaFunctions.setFolderPermissions,
    "addconfig": SambaFunctions.addShareConfig,
    "shares": SambaFunctions.listShares,
    "testconf": SambaFunctions.testConfig,
    "connections": SambaFunctions.listConnections,
    "perms": SambaFunctions.folderPermissions,
    "files": SambaFunctions.listSharedFiles,
    "help": SambaFunctions.helptext,
    "helpf": SambaFunctions.helptextfull,
    "quit": quit,
}

SAMBA_ALIASES = {
    "i": "install",
    "st": "start",
    "sp": "stop",
    "e": "enable",
    "d": "disable",
    "r": "restart",
    "s": "status",
    "au": "adduser",
    "ru": "removeuser",
    "eu": "enableuser",
    "du": "disableuser",
    "ms": "mkshare",
    "rs": "rmshare",
    "o": "owner",
    "c": "chmod",
    "ac": "addconfig",
    "ls": "shares",
    "tc": "testconf",
    "con": "connections",
    "p": "perms",
    "f": "files",
    "h": "help",
    "hf": "helpf",
    "q": "quit",
}

def root_help():
    print("""
    Command     Alias   Description

    user        (u)     User management
    group       (g)     Group management
    ssh         (ss)     SSH setup
    samba       (sa)    Samba setup
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

# add apache setup
# add errorhandling ; user permission managment ; foldere permissions
