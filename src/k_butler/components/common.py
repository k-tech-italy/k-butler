from PyQt6.QtWidgets import QMessageBox, QTextEdit, QToolBox, QGroupBox, QVBoxLayout, QPushButton, QHBoxLayout


class GuiModal(QMessageBox):
    def __init__(self, title: str, message: str = '', ):
        """
        Simple modal window for displaying a message.
        """
        super().__init__()
        self.setWindowTitle(title)
        self.setText(message)
        self.setModal(True)
        self._open_modal()

    def _open_modal(self):
        self.exec()


class GuiTextEdit(QTextEdit):

    def __init__(self, text='', ):
        super().__init__()
        self.setReadOnly(False)
        self.setPlainText(text)

    def setPlainText(self, text):
        super().setPlainText(text)


class GuiAccordionItem(QGroupBox):
    def __init__(self,  strategy, on_click, ):
        super().__init__()
        main_layout = QHBoxLayout(self)

        button_layout = QVBoxLayout()
        for action in strategy.actions:
            button = QPushButton(action)
            button.setDefault(True)
            button.clicked.connect(lambda checked, a=action: on_click(action=a, strategy=strategy))
            button_layout.addWidget(button)

        button_layout.addStretch(1)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()


class GuiAccordion(QToolBox):
    """
    A GUI component that is a toolbox with expandable items.
    Each item is a group of buttons related to a specific strategy.
    """

    def __init__(self, items: dict, on_click_button, *args, **kwargs):
        """
        Args:
            items (dict): A dictionary of items where each key is the name of the item and
                the value is a strategy object.
        """
        super().__init__()
        for item in items:
            self.addItem(GuiAccordionItem(items[item], on_click_button), item)
