from pyperclip import copy
from PyQt6.QtCore import pyqtSlot


class ClipboardStrategy:
    name = 'Clipboard processor'
    description = ''
    actions = {
        'copy': 'copy to clipboard',
    }

    @pyqtSlot()
    def copy(self, text):
        copy(text)
