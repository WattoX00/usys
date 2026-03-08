# USYS – Linux User Manager

USYS is a simple command-line Linux user and group management tool.
It provides an interactive interface to manage users and groups using
clear commands and short aliases.

## Features

- Create, modify, and delete users
- Create and manage groups
- Add users to groups
- View user and group information
- Simple command aliases for faster usage

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

```bash
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
```

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

