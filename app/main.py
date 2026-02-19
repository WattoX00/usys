from functions import Functions

from commands import USER_COMMANDS, USER_ALIASES, GROUP_COMMANDS, GROUP_ALIASES, COMMAND_SETS

def main():
    # main loop
    
    ROOT_COMMANDS = {}

    while True:
        try:
            raw = str(input('usys ~ $ ')).strip().lower()
        except KeyboardInterrupt:
            break

        if not raw:
            continue

        if raw in COMMAND_SETS:
            run_mode(raw)
            continue
        print(f"{raw}: commands not found")

def run_mode(mode):
    commands, aliases = COMMAND_SETS[mode]

    while True:
        try:
            raw = str(input(f'{mode} ~ $ ')).strip().lower()
        except KeyboardInterrupt:
            print()
            return

        if not raw:
            continue

        if raw == 'exit':
            return

        command = aliases.get(raw, raw)
        func = commands.get(command)

        if not func:
            print(f'{command}: command not found')
            continue

        func()

main()
