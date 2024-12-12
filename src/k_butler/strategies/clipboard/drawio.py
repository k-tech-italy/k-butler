from PyQt6.QtCore import pyqtSlot
import pyperclip

from k_butler.components.common import create_error_modal


class DrawioCreateTableParse:
    name = 'Drawio SQL Create Table parser for ERD'
    description = ''
    actions = {
        'copy': 'copy to clipboard',
        'paste': 'paste from clipboard',
        'parse': 'parse clipboard',
    }

    def __init__(self):
        self.start = None

    def match(self, text: str) -> bool:
        self.start = 'CREATE TABLE '
        return text.upper().startswith(self.start)

    @pyqtSlot()
    def parse(self, component):
        text = component.editor.toPlainText()
        match = self.match(text)
        if not match:
            return create_error_modal(self.start, 'Copy a string that starts with:')
        result = f'{text}_1'
        pyperclip.copy(result)
        component.editor.setPlainText(result)

    @pyqtSlot()
    def paste(self, component):
        text = pyperclip.paste()
        match = self.match(text)
        if not match:
            return create_error_modal(self.start, 'Copy a string that starts with:')
        component.editor.setPlainText(text)
