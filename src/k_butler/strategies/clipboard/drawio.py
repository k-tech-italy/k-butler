import pyperclip

from k_butler.strategies.clipboard.base import ClipboardStrategyBase


class DrawioCreateTableConfigurator:
    name = 'Drawio SQL Create Table parser for ERD'
    pass


class DrawioCreateTableParse(ClipboardStrategyBase):
    name = 'Drawio SQL Create Table parser for ERD'
    key = 'drawio_parse'
    description = ''
    actions = {
        'copy': 'copy to clipboard',
        'paste': 'paste from clipboard',
        'parse': 'parse clipboard',
    }

    configurator = DrawioCreateTableConfigurator

    def __init__(self):
        super().__init__()

    def matches(self, text: str) -> bool:
        """
        Check if the text is a SQL create table statement.
        """
        try:
            prefix = 'CREATE TABLE '
            if not text.upper().startswith(prefix):
                raise ValueError(f"Text does not start with '{prefix}'")
        except ValueError as e:
            raise e
        return True

    def parse(self, text):
        """
        Parse the text into a SQL create table statement. WIP
        """
        if self.matches(text):
            result = f'{text}_1'
            pyperclip.copy(result)
            return result

    def paste(self, *args, **kwargs):
        """Paste the last copied text"""
        text = pyperclip.paste()
        return text

    def copy(self, text: str):
        """Copy the text to the clipboard"""
        pyperclip.copy(text)
        return text

    def get_action(self, *args, **kwargs):
        action = getattr(self, kwargs['action'])
        return action(kwargs['text'])
