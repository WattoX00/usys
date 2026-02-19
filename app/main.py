from functions import Functions
from commands import USER_COMMANDS, USER_ALIASES, GROUP_COMMANDS, GROUP_ALIASES, COMMAND_SETS, ROOT_COMMANDS, ROOT_ALIASES
from shell import run_shell

def main():
    run_shell("usys ~ $ ", ROOT_COMMANDS, ROOT_ALIASES)


main()
