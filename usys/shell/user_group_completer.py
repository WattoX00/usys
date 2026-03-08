from prompt_toolkit.completion import Completer, Completion
from ..functions.functions import HelpFunctions


class UserGroupCompleter(Completer):

    def __init__(self, mode):
        self.mode = mode

    def get_completions(self, document, complete_event):
        text = document.get_word_before_cursor()

        if self.mode == "users":
            options = HelpFunctions.getUsers()
        elif self.mode == "groups":
            options = HelpFunctions.getGroups()
        else:
            options = []

        for option in options:
            if option.startswith(text):
                yield Completion(option, start_position=-len(text))
