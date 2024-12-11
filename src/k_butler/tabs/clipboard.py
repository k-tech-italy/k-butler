from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

from k_butler.strategies.clipboard import ClipboardStrategy


class Clipboard(QWidget):
    tabLabel = 'Clipboard'
    strategy = ClipboardStrategy

    def __init__(self, parent=..., *args):
        super().__init__(parent, *args)
        main_layout = QVBoxLayout()
        editor = QTextEdit()

        main_layout.addWidget(editor)

        button = QPushButton('Copy')
        main_layout.addWidget(button)
        button.clicked.connect(lambda: ClipboardStrategy.copy(self, editor.toPlainText()))

        self.setLayout(main_layout)
