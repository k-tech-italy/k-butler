from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QGroupBox, QGridLayout

from k_butler.strategies.clipboard.drawio import DrawioCreateTableParse


class Clipboard(QWidget):
    tabLabel = 'Clipboard'
    strategy = DrawioCreateTableParse

    def __init__(self, parent=..., *args):
        super().__init__(parent, *args)
        main_layout = QVBoxLayout()
        self.editor = QTextEdit()

        main_layout.addWidget(self.editor)

        button_layout = QGroupBox('Actions')
        layout = QGridLayout()

        button = QPushButton('Parse')
        layout.addWidget(button)
        button.clicked.connect(lambda: DrawioCreateTableParse().parse(component=self))

        button = QPushButton('Paste from clipboard')
        layout.addWidget(button)
        button.clicked.connect(lambda: DrawioCreateTableParse().paste(component=self))

        button_layout.setLayout(layout)
        main_layout.addWidget(button_layout)
        self.setLayout(main_layout)
