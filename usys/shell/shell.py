from prompt_toolkit import PromptSession
from .dictcompleter import DictCompleter

def run_shell(prompt, commands, aliases):

    session = PromptSession()

    completer = DictCompleter(
        commands,
        extra_commands=["exit"]
    )

    while True:
        try:
            raw = session.prompt(
                prompt,
                completer=completer,
            ).strip().lower()
        except KeyboardInterrupt:
            print()
            return

        if not raw:
            continue

        if raw in ('exit', 'e'):
            return

        command = aliases.get(raw, raw)
        func = commands.get(command)

        if not func:
            print(f"{command}: command not found")
            continue

        func()
