from prompt_toolkit.completion import Completer, Completion

class DictCompleter(Completer):
    def __init__(self, commands: dict, extra_commands=None):
        self.commands = commands
        self.extra_commands = extra_commands or []

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lower()

        if " " in text:
            return

        words = (
            list(self.commands.keys())
            + self.extra_commands
        )

        for word in words:
            if word.startswith(text):
                yield Completion(word, start_position=-len(text))
