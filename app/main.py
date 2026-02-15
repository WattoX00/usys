from functions import Functions

from commands import COMMANDS, ALIASES

def main():
    # main loop

    while True:
        try:
            raw = str(input('todol ~ $ ')).strip()
        except KeyboardInterrupt:
            break

        if not raw:
            continue

        command = raw.lower()
        command = ALIASES.get(command, command)

        func = COMMANDS.get(command)

        if not func:
            print(f'{command}: command not found')
            continue
        func()

main()
