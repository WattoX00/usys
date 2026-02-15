from functions import Functions

from commands import COMMANDS

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

        func = COMMANDS.get(command)

        if not func:
            print(f'{command}: command not found')
            continue
        func()

main()
