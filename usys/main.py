from .shell.shell import run_shell
from .shell.dictcompleter import DictCompleter
from .functions.commands import USER_COMMANDS, USER_ALIASES, GROUP_COMMANDS, GROUP_ALIASES, root_help, helpFull
from prompt_toolkit import PromptSession
def main():
    session = PromptSession()

    root_commands = [
        "exit", "q", "e",
        "help", "h",
        "helpf", "hf",
        "user", "u",
        "group", "g"
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

        print(f"{raw}: command not found")
main()
