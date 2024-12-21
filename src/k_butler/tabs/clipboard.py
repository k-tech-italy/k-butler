from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QGroupBox, QGridLayout

from k_butler.components.common import GuiAccordion
from k_butler.strategies.clipboard.drawio import DrawioCreateTableParse


class Clipboard(QWidget):
    tabLabel = 'Clipboard'
    strategy = DrawioCreateTableParse

    def __init__(self, parent=..., *args):
        super().__init__(parent, *args)
        main_layout = QVBoxLayout()
        self.editor = QTextEdit()

        main_layout.addWidget(self.editor)
        strategies = {self.strategy.key: self.strategy}

        button_layout = QGroupBox('Actions')
        layout = QGridLayout()
        strategy_toolbox = GuiAccordion(self.editor.setText, strategies=strategies)

        layout.addWidget(strategy_toolbox, 1, 1)
        layout.addWidget(self.editor, 1, 2)

        button_layout.setLayout(layout)
        main_layout.addWidget(button_layout)
        self.setLayout(main_layout)
