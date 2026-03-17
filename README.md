# USYS – Linux User Manager

[![Version](https://img.shields.io/badge/version-0.1.3-blue?style=for-the-badge)](https://github.com/WattoX00/usys/releases/tag/v0.1.3)
![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=for-the-badge)
[![PyPI](https://img.shields.io/pypi/v/usys?style=for-the-badge)](https://pypi.org/project/usys/)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)
![Build](https://img.shields.io/github/actions/workflow/status/wattox00/usys/publish.yml?style=for-the-badge)
[![License](https://img.shields.io/github/license/wattox00/usys?style=for-the-badge)](https://github.com/WattoX00/usys/blob/main/LICENSE)

USYS is a simple command-line Linux user and group management tool.
It provides an interactive interface to manage users and groups using
clear commands and short aliases.

<details>
<summary>📚 Contents</summary>
  
- [Installation](#installation)
- [Features](#features)
- [Disclaimer](#disclaimer)
- [Usage](#usage)
- [Commands](#commands)
- [Support](#support)
- [License](#license)

</details>

## Features

- Create, modify, and delete users
- Create and manage groups
- Add users to groups
- View user and group information
- Simple command aliases for faster usage

## Disclaimer:
This program may not always work as intended. Use it at your own risk,
especially in production environments or large projects.

The program was primarily tested on Arch Linux. Other Linux distributions
may behave differently.

Most operations require sudo permissions (except for listing functions),
so make sure you understand what the program does before using it.

## Usage:
Navigate between shells using their commands. For example, type
'user' or 'u' to enter the user shell mode. Inside each shell you can
execute commands related to that category. Each shell also provides
its own help functions.

## Commands:
<details>
<summary>Click to open</summary>

  
### 📦 Root Commands
These commands switch you into dedicated management shells:

| Alias | Command      | Description                       |
| ----- | ------------ | --------------------------------- |
| `u`   | `user`       | Enter user management shell       |
| `g`   | `group`      | Enter group management shell      |
| `p`   | `permission` | Enter permission management shell |
| `ss`  | `ssh`        | Enter SSH setup shell             |
| `sa`  | `samba`      | Enter Samba setup shell           |
| `a`   | `apache`     | Enter Apache setup shell          |
| `h`   | `help`       | Show root help menu               |
| `q`   | `exit`       | Exit program                      |

### 👤 User Commands

| Alias | Command          | Description             |
| ----- | ---------------- | ----------------------- |
| `au`  | `adduser`        | Create a new user       |
| `du`  | `deluser`        | Delete a user           |
| `pw`  | `passwd`         | Change user password    |
| `ag`  | `appendgroup`    | Add user to group       |
| `ar`  | `rmfgroup`       | Remove user from group  |
| `cn`  | `chname`         | Change username         |
| `cs`  | `chshell`        | Change user shell       |
| `luu` | `lockuser`       | Lock user account       |
| `ulu` | `unlockuser`     | Unlock user account     |
| `se`  | `setexp`         | Set account expiration  |
| `re`  | `rmexp`          | Remove expiration       |
| `uid` | `chuid`          | Change user ID          |
| `lu`  | `listusers`      | List all users          |
| `lug` | `listusergroups` | List user's groups      |
| `hd`  | `homedir`        | Show home directory     |
| `pi`  | `passinfo`       | Show password info      |
| `ul`  | `userlocked`     | Check if locked         |
| `ued` | `userexpday`     | Show expiration day     |
| `idu` | `iduser`         | Show user ID info       |
| `gu`  | `getentuser`     | Get user from system DB |
| `h`   | `help`           | Help menu               |
| `hf`  | `helpf`          | Full help               |
| `q`   | `quit`           | Exit shell              |

### 👥 Group Commands

| Alias | Command      | Description                |
| ----- | ------------ | -------------------------- |
| `ga`  | `addgroup`   | Create new group           |
| `gr`  | `rmgroup`    | Remove group (from system) |
| `cg`  | `chgroup`    | Rename group               |
| `gd`  | `delgroup`   | Delete group               |
| `lg`  | `listgroups` | List all groups            |
| `gid` | `chgid`      | Change group ID            |
| `gi`  | `groupinfo`  | Show group info            |
| `h`   | `help`       | Help menu                  |
| `hf`  | `helpf`      | Full help                  |
| `q`   | `quit`       | Exit shell                 |

### 🔐 Permission Commands

| Alias | Command    | Description             |
| ----- | ---------- | ----------------------- |
| `v`   | `view`     | View permissions        |
| `c`   | `chmod`    | Change file permissions |
| `co`  | `chown`    | Change file owner       |
| `cg`  | `chgrp`    | Change group ownership  |
| `au`  | `adduser`  | Add user permission     |
| `ag`  | `addgroup` | Add group permission    |
| `ru`  | `rmuser`   | Remove user permission  |
| `rg`  | `rmgroup`  | Remove group permission |
| `rc`  | `rchmod`   | Recursive chmod         |
| `rco` | `rchown`   | Recursive chown         |
| `rcg` | `rchgrp`   | Recursive chgrp         |
| `h`   | `help`     | Help menu               |
| `hf`  | `helpf`    | Full help               |
| `q`   | `quit`     | Exit shell              |

### 🔑 SSH Commands

| Alias | Command    | Description         |
| ----- | ---------- | ------------------- |
| `i`   | `install`  | Install OpenSSH     |
| `e`   | `enable`   | Enable SSH service  |
| `gk`  | `genkey`   | Generate SSH key    |
| `lk`  | `listkeys` | List SSH keys       |
| `gh`  | `github`   | Setup GitHub SSH    |
| `t`   | `test`     | Test SSH connection |
| `s`   | `setup`    | Full SSH setup      |
| `h`   | `help`     | Help menu           |
| `hf`  | `helpf`    | Full help           |
| `q`   | `quit`     | Exit shell          |

### 📁 Samba Commands

| Alias | Command       | Description            |
| ----- | ------------- | ---------------------- |
| `i`   | `install`     | Install Samba          |
| `st`  | `start`       | Start Samba service    |
| `sp`  | `stop`        | Stop Samba             |
| `e`   | `enable`      | Enable Samba           |
| `d`   | `disable`     | Disable Samba          |
| `r`   | `restart`     | Restart Samba          |
| `s`   | `status`      | Service status         |
| `au`  | `adduser`     | Add Samba user         |
| `ru`  | `removeuser`  | Remove Samba user      |
| `eu`  | `enableuser`  | Enable Samba user      |
| `du`  | `disableuser` | Disable Samba user     |
| `ms`  | `mkshare`     | Create shared folder   |
| `rs`  | `rmshare`     | Remove shared folder   |
| `o`   | `owner`       | Set folder owner       |
| `c`   | `chmod`       | Set folder permissions |
| `ac`  | `addconfig`   | Add share config       |
| `ls`  | `shares`      | List shares            |
| `tc`  | `testconf`    | Test config            |
| `con` | `connections` | Active connections     |
| `p`   | `perms`       | Folder permissions     |
| `f`   | `files`       | List shared files      |
| `h`   | `help`        | Help menu              |
| `hf`  | `helpf`       | Full help              |
| `q`   | `quit`        | Exit shell             |

### 🌐 Apache Commands

| Alias | Command      | Description           |
| ----- | ------------ | --------------------- |
| `i`   | `install`    | Install Apache        |
| `x`   | `extras`     | Install extra modules |
| `st`  | `start`      | Start Apache          |
| `sp`  | `stop`       | Stop Apache           |
| `r`   | `restart`    | Restart Apache        |
| `ss`  | `status`     | Check status          |
| `ct`  | `configtest` | Test configuration    |
| `ts`  | `testsite`   | Create test site      |
| `vh`  | `vhost`      | Create virtual host   |
| `en`  | `enable`     | Enable site           |
| `di`  | `disable`    | Disable site          |
| `al`  | `accesslog`  | View access log       |
| `el`  | `errorlog`   | View error log        |
| `h`   | `help`       | Help menu             |
| `hf`  | `helpf`      | Full help             |
| `q`   | `quit`       | Exit shell            |

</details>

## Flags (run outside USYS):
usys --version     Show the installed version
usys --update      Check for updates and install if available
usys --helpf       Show full help message

## Documentation and source code:
[https://github.com/WattoX00/usys](https://github.com/WattoX00/usys)
[https://pypi.org/project/usys/](https://pypi.org/project/usys/)

If you encounter any issues, please report them here:
[https://github.com/WattoX00/usys/issues](https://github.com/WattoX00/usys/issues)

Thank you for using USYS!

## ❤️ Support

If this project saved you time, taught you something, or made your day a little easier,
you can support its development here:

👉 **[Buy me a coffee via PayPal](https://www.paypal.com/paypalme/wattox)**

Your support helps keep the project:
- Actively maintained
- Continuously improved
- Free and open source

Thanks for being part of the community 🤝
