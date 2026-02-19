from shell import run_shell
from commands import USER_COMMANDS, USER_ALIASES, GROUP_COMMANDS, GROUP_ALIASES

def root_help():
    print("\nAvailable modes:")
    print("  user")
    print("  group")
    print("  help")
    print("  exit\n")

def main():
    while True:
        try:
            raw = input("usys ~ $ ").strip().lower()
        except KeyboardInterrupt:
            print()
            break

        if not raw:
            continue

        if raw == "exit":
            break

        if raw == "help" or raw == "h":
            root_help()
            continue

        if raw == "user":
            run_shell("user ~ $ ", USER_COMMANDS, USER_ALIASES)
            continue

        if raw == "group":
            run_shell("group ~ $ ", GROUP_COMMANDS, GROUP_ALIASES)
            continue

        print(f"{raw}: command not found")

main()
