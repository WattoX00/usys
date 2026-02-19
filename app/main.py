from functions import Functions

from commands import COMMANDS, ALIASES

def main():
    # main loop

    while True:
        try:
            raw = str(input('usys ~ $ ')).strip()
        except KeyboardInterrupt:
            break

        if not raw:
            continue

        command = raw.lower()
        

        command = active_aliases.get(command, command)
        func = active_commands.get(command)

        if not func:
            print(f'{command}: command not found')
            continue
        func()

main()
