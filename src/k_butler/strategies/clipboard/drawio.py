from PyQt6.QtCore import pyqtSlot


class DrawioCreateTableParse:
    name = 'Drawio SQL Create Table parser for ERD'
    description = ''
    actions = {
        'copy': 'copy to clipboard',
    }

    def match(self, text: str) -> bool:
        return text.upper().startswith('CREATE TABLE ')

    @pyqtSlot()
    def parse(self, text):
        text = paperclip.paste()
        result = f'{text}_1'
        paperclip.copy(result)
        # TODO: put result in UI textarea (RO?)
