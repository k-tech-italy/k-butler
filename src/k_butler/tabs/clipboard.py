from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout

from k_butler.components.common import GuiAccordion, GuiModal, GuiTextEdit
from k_butler.strategies.clipboard.drawio import DrawioCreateTableParse
import pyperclip


class Clipboard(QWidget):
    tabLabel = 'Clipboard'
    strategy = DrawioCreateTableParse()

    def __init__(self, parent=..., *args):
        super().__init__(parent, *args)
        main_layout = QVBoxLayout()
        self.clipboard_text = pyperclip.paste()

        self.editor = GuiTextEdit(self.clipboard_text)

        items = {self.strategy.key: self.strategy}

        self.actions_layout = QGroupBox('Actions')
        layout = QGridLayout()
        self.strategy_toolbox = GuiAccordion(items, self.action_clipboard)

        layout.addWidget(self.strategy_toolbox, 1, 1)
        layout.addWidget(self.editor, 1, 2)

        self.actions_layout.setLayout(layout)
        main_layout.addWidget(self.actions_layout)
        self.setLayout(main_layout)

    def action_clipboard(self, *args, **kwargs):
        action = kwargs['action']
        text = self.editor.toPlainText()
        try:
            res = self.strategy.get_action(action=action, text=text)
            self.editor.setText(res)
        except Exception as e:
            GuiModal('error', f'{e}')
