from functions import Functions

from .functionality.prompts import Prompts
from commands import COMMANDS
from .functionality.commands import Commands

def main():
    # main loop

    while True:
        try:
            raw = Prompts.session.prompt('todol ~ $ ').strip()
        except KeyboardInterrupt:
            break

        if not raw:
            continue

        parts = raw.split()
        command, *args = parts
        command = command.lower()

        func = COMMANDS.get(command)

        if not func:
            print(f'{command}: command not found')
            continue

        try:
            func(args)
        except IndexError:
            print('Missing argument')
        except (SystemExit, KeyboardInterrupt):
            break
main()
