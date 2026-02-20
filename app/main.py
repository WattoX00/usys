from shell import run_shell
from functions.commands import USER_COMMANDS, USER_ALIASES, GROUP_COMMANDS, GROUP_ALIASES, root_help, helpFull

def main():
    while True:
        try:
            raw = input("usys ~ $ ").strip().lower()
        except KeyboardInterrupt:
            print()
            break

        if not raw:
            continue

        if raw == 'exit' or raw == 'q' or raw == 'e':
            break

        if raw == 'help' or raw == 'h':
            root_help()
            continue

        if raw == 'helpf' or raw == 'hf':
            helpFull()
            continue

        if raw == 'user' or raw == 'u':
            run_shell('usys user ~ $ ', USER_COMMANDS, USER_ALIASES)
            continue

        if raw == 'group' or raw == 'g':
            run_shell('usys group ~ $ ', GROUP_COMMANDS, GROUP_ALIASES)
            continue

        print(f"{raw}: command not found")

main()
