# for flags
import argparse
from .flags.update import Update
from .flags.verison import Version

# for while loop inside usys executable
from .shell.shell import run_shell
from .shell.dictcompleter import DictCompleter
from .functions.commands import USER_COMMANDS, USER_ALIASES, GROUP_COMMANDS, GROUP_ALIASES, PERMISSION_COMMANDS, PERMISSION_ALIASES, SSH_COMMANDS, SSH_ALIASES, SAMBA_COMMANDS, SAMBA_ALIASES, APACHE_COMMANDS, APACHE_ALIASES, root_help, helpFull
from prompt_toolkit import PromptSession


def parse_args():
    parser = argparse.ArgumentParser(
        prog="usys",
        description=f"{TodolVersion.version()}\nLinux User Manager :)",
        formatter_class=argparse.RawTextHelpFormatter
    )

    info = parser.add_argument_group("Information")
    info.add_argument("-u", "--update", action="store_true", help="Update todol with pipx")
    info.add_argument("-v", "--version", action="store_true", help="Show version")

    return parser.parse_args()

def main():
    # flag handling

    args = parse_args()
 
    if args.update:
        Update.update()
        return

    if args.version:
        print(Version.version())
        return

    # main loop

    session = PromptSession()

    root_commands = [
        "exit",
        "help",
        "helpf",
        "user",
        "group",
        "permission",
        "ssh",
        "samba",
        "apache",
    ]

    completer = DictCompleter({}, root_commands)

    while True:
        try:
            raw = session.prompt(
                "usys ~ $ ",
                completer=completer,
            ).strip().lower()
        except KeyboardInterrupt:
            print()
            break

        if not raw:
            continue

        if raw in ('exit', 'q', 'e'):
            break

        if raw in ('help', 'h'):
            root_help()
            continue

        if raw in ('helpf', 'hf'):
            helpFull()
            continue

        if raw in ('user', 'u'):
            run_shell('usys user ~ $ ', USER_COMMANDS, USER_ALIASES)
            continue

        if raw in ('group', 'g'):
            run_shell('usys group ~ $ ', GROUP_COMMANDS, GROUP_ALIASES)
            continue

        if raw in ('permission', 'p'):
            run_shell('usys permission ~ $ ', PERMISSION_COMMANDS, PERMISSION_ALIASES)
            continue

        if raw in ('ssh', 'ss'):
            run_shell('usys ssh ~ $ ', SSH_COMMANDS, SSH_ALIASES)
            continue

        if raw in ('samba', 'sa'):
            run_shell('usys samba ~ $ ', SAMBA_COMMANDS, SAMBA_ALIASES)
            continue

        if raw in ('apache', 'a'):
            run_shell('usys apache ~ $ ', APACHE_COMMANDS, APACHE_ALIASES)
            continue

        print(f"{raw}: command not found")
main()
