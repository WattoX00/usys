from .functions import HelpFunctions
from .user_cfg import UserFunctions
from .group_cfg import GroupFunctions
from .permission_cfg import PermissionFunctions
from .ssh_cfg import SSHFunctions
from .samba_cfg import SambaFunctions
from .apache_cfg import ApacheFunctions

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

PERMISSION_COMMANDS = {
    "view": PermissionFunctions.viewPermissions,
    "chmod": PermissionFunctions.chmodPermissions,
    "chown": PermissionFunctions.changeOwner,
    "chgrp": PermissionFunctions.changeGroup,
    "adduser": PermissionFunctions.addUserPermission,
    "addgroup": PermissionFunctions.addGroupPermission,
    "rmuser": PermissionFunctions.removeUserPermission,
    "rmgroup": PermissionFunctions.removeGroupPermission,
    "rchmod": PermissionFunctions.recursivePermissions,
    "rchown": PermissionFunctions.recursiveOwner,
    "rchgrp": PermissionFunctions.recursiveGroup,
    "help": PermissionFunctions.helptext,
    "helpf": PermissionFunctions.helptext,
    "quit": quit,
}

PERMISSION_ALIASES = {
    "v": "view",
    "c": "chmod",
    "co": "chown",
    "cg": "chgrp",
    "au": "adduser",
    "ag": "addgroup",
    "ru": "rmuser",
    "rg": "rmgroup",
    "rc": "rchmod",
    "rco": "rchown",
    "rcg": "rchgrp",
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
    "helpf": SSHFunctions.helptext,
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
    "hf": "helpf",
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

APACHE_COMMANDS = {
    "install": ApacheFunctions.installApacheBasic,
    "extras": ApacheFunctions.installApacheExtras,
    "start": ApacheFunctions.apacheStart,
    "stop": ApacheFunctions.apacheStop,
    "restart": ApacheFunctions.apacheRestart,
    "status": ApacheFunctions.apacheStatus,
    "configtest": ApacheFunctions.apacheConfigTest,
    "testsite": ApacheFunctions.apacheCreateTestSite,
    "vhost": ApacheFunctions.apacheCreateVHost,
    "enable": ApacheFunctions.apacheEnableSite,
    "disable": ApacheFunctions.apacheDisableSite,
    "accesslog": ApacheFunctions.apacheAccessLog,
    "errorlog": ApacheFunctions.apacheErrorLog,
    "help": ApacheFunctions.helptext,
    "helpf": ApacheFunctions.helptextfull,
    "quit": quit,
}

APACHE_ALIASES = {
    "i": "install",
    "x": "extras",
    "st": "start",
    "sp": "stop",
    "r": "restart",
    "ss": "status",
    "ct": "configtest",
    "ts": "testsite",
    "vh": "vhost",
    "en": "enable",
    "di": "disable",
    "al": "accesslog",
    "el": "errorlog",
    "h": "help",
    "hf": "helpf",
    "q": "quit",
}

def root_help():
    print("""
    Shells:

    user        (u)     User management
    group       (g)     Group management
    permission  (p)     Permission management
    ssh         (ss)    SSH setup
    samba       (sa)    Samba setup
    apache      (a)     Apache setup

    help        (h)     Show this help menu
    exit        (q)     Exit the program
    """)

def helpFull():
    from ..flags.version import UsysVersion
    print(f"""
    USYS - Linux user manager :)
    Version {UsysVersion.version()}

    Disclaimer:
    This program may not always work as intended. Use it at your own risk,
    especially in production environments or large projects.

    The program was primarily tested on Arch Linux. Other Linux distributions
    may behave differently.

    Most operations require sudo permissions (except for listing functions),
    so make sure you understand what the program does before using it.

    Usage:
    Navigate between shells using their commands. For example, type
    'user' or 'u' to enter the user shell mode. Inside each shell you can
    execute commands related to that category. Each shell also provides
    its own help functions.

    Shells:
    user        (u)     User management
    group       (g)     Group management
    permission  (p)     Permission management
    ssh         (ss)    SSH setup
    samba       (sa)    Samba setup
    apache      (a)     Apache setup

    help        (h)     Show the short help menu
    helpf       (hf)    Show this full help menu
    exit        (q)     Exit the program

    Flags (run outside USYS):
    usys --version     Show the installed version
    usys --update      Check for updates and install if available
    usys --helpf       Show this full help message

    Documentation and source code:
    https://github.com/WattoX00/usys
    https://pypi.org/project/usys/

    If you encounter any issues, please report them here:
    https://github.com/WattoX00/usys/issues

    Thank you for using USYS!
    """)

# todo :

# add flags

