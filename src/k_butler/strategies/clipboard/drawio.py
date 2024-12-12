from PyQt6.QtCore import pyqtSlot
import pyperclip


class DrawioCreateTableParse:
    name = 'Drawio SQL Create Table parser for ERD'
    description = ''
    actions = {
        'copy': 'copy to clipboard',
        'parse': 'parse clipboard',
    }

    def match(self, text: str) -> bool:
        return text.upper().startswith('CREATE TABLE ')

    @pyqtSlot()
    def parse(self, parent):
        text = pyperclip.paste()
        match = self.match(text)

        result = f'{text}_1'
        pyperclip.copy(result)
        parent.editor.setPlainText(result)
