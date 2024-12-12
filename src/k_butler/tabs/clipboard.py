from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

from k_butler.strategies.clipboard.drawio import DrawioCreateTableParse
import pyperclip


class Clipboard(QWidget):
    tabLabel = 'Clipboard'
    strategy = DrawioCreateTableParse

    def __init__(self, parent=..., *args):
        super().__init__(parent, *args)
        main_layout = QVBoxLayout()
        self.editor = QTextEdit()
        self.editor.setPlainText(pyperclip.paste())
        self.editor.setReadOnly(True)

        main_layout.addWidget(self.editor)

        button = QPushButton('Parse')
        main_layout.addWidget(button)
        button.clicked.connect(lambda: DrawioCreateTableParse.parse(self, parent=self))

        self.setLayout(main_layout)
