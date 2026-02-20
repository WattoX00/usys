def run_shell(prompt, commands, aliases):
    while True:
        try:
            raw = input(prompt).strip().lower()
        except KeyboardInterrupt:
            print()
            return

        if not raw:
            continue

        if raw == 'exit' or raw == 'e':
            return

        command = aliases.get(raw, raw)
        func = commands.get(command)

        if not func:
            print(f"{command}: command not found")
            continue

        func()
