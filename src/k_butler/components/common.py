from PyQt6.QtWidgets import QMessageBox, QTextEdit, QToolBox, QGroupBox, QVBoxLayout, QPushButton, QHBoxLayout

from k_butler.configuration import ConfigStorage


class GuiModal(QMessageBox):
    def __init__(self, message, second_message='', ):
        super().__init__()
        self.setWindowTitle(message)
        self.setText(f"{message} {second_message}")
        self.setModal(True)
        self.exec()


class GuiTextEdit(QTextEdit):

    def __init__(self, text='', ):
        super().__init__()
        self.setReadOnly(False)
        self.setPlainText(text)

    def setPlainText(self, text):
        super().setPlainText(text)




class GuiAccordion(QToolBox):
    def __init__(self, update_text=None, files_bo=None, strategies=None):
        """
        Creates a QToolBox widget populated with action buttons.
        Single File = each action button for each strategy
        Multiple Files = Group action for group strategy
        """
        super().__init__()

        self.update_text = update_text
        if strategies is not None and files_bo is None:
            for strategy in strategies:
                self.addItem(self.create_buttons_config(strategies[strategy]), strategy)

        if files_bo is not None:
            self.file_bos = files_bo
            for file_bo in self.file_bos:
                for handler in file_bo.handlers:
                    self.addItem(self.create_buttons_actions(handler, file_bo), handler.name)

    def create_buttons_config(self, strategy):
        def read_config():
            storage = ConfigStorage(strategy.key)
            res = storage.read()
            if self.update_text is not None:
                self.update_text(str(res), strategy.key)

        configurator = strategy.configurator
        buttons_component = QGroupBox(configurator.name)
        button_layout = QVBoxLayout()

        button = QPushButton('Configuration')
        button.setDefault(True)
        button.clicked.connect(lambda checked: read_config())
        button_layout.addWidget(button)

        button_layout.addStretch(1)
        main_layout = QHBoxLayout(buttons_component)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        return buttons_component

    def create_buttons_actions(self, strategy, file_bo):  # TODO manage multiple files
        """
        Creates a QToolBox widget populated with action buttons.
        Single File = each action button for each strategy
        Multiple Files = Group action for group strategy
        """
        buttons_component = QGroupBox("Actions")
        button_layout = QVBoxLayout()

        for action in strategy.actions:
            button = QPushButton(action)
            button.setDefault(True)
            button.clicked.connect( lambda checked, a=action, f=file_bo: strategy.get_action(a, file_bo))
            button_layout.addWidget(button)

        button_layout.addStretch(1)
        main_layout = QHBoxLayout(buttons_component)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        return buttons_component

