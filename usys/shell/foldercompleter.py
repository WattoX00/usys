import os
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import PathCompleter

class PromptToolkitSession:

    @staticmethod
    def folderPrompt(base_path=None):
        session = PromptSession()

        completer = PathCompleter(
            only_directories=True,
            expanduser=True
        )

        try:
            folder = session.prompt(
                "Folder: ",
                completer=completer,
                complete_while_typing=True
            ).strip()
        except KeyboardInterrupt:
            print("\nCancelled.")
            return None

        if not folder and base_path:
            folder = base_path

        folder = os.path.abspath(os.path.expanduser(folder))

        if base_path and not os.path.isabs(folder):
            folder = os.path.join(base_path, folder)

        return folder

