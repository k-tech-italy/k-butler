from PyQt6.QtWidgets import QMessageBox, QTextEdit, QToolBox, QGroupBox, QVBoxLayout, QPushButton, QHBoxLayout

from k_butler.configuration import ConfigStorage
from k_butler.strategies.base import Registry


def create_error_modal(name, error_message='generic error'):
    modal = QMessageBox()
    modal.setWindowTitle(error_message)
    modal.setText(f"{error_message} {name}")
    modal.setModal(True)
    modal.exec()


class GuiTextEdit(QTextEdit):

    def __init__(self, text='', ):
        super().__init__()
        self.setReadOnly(False)
        self.setPlainText(text)

    def setPlainText(self, text):
        super().setPlainText(text)


def create_buttons_actions(strategy, file_bo):  # TODO manage multiple files
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
        button.clicked.connect(lambda checked, a=action: strategy.get_action(a, file_bo))
        button_layout.addWidget(button)

    button_layout.addStretch(1)
    main_layout = QHBoxLayout(buttons_component)
    main_layout.addLayout(button_layout)
    main_layout.addStretch()

    return buttons_component


class GuiAccordion(QToolBox):
    def __init__(self, update_action_detail, updateText=None, files_bo=None, strategies=None):
        """
        Creates a QToolBox widget populated with action buttons.
        Single File = each action button for each strategy
        Multiple Files = Group action for group strategy
        """
        super().__init__()

        self.updateText = updateText
        if strategies is not None:
            for strategy in strategies:
                self.addItem(self.create_buttons_config(strategies[strategy]), strategy)

        if files_bo is not None:
            self.file_bos = files_bo
            for file_bo in self.file_bos:
                for handler in file_bo.handlers:
                    self.addItem(create_buttons_actions(handler, file_bo, update_action_detail), handler.name)

    def create_buttons_config(self, strategy):
        def read_config():
            storage = ConfigStorage(strategy.key)
            res = storage.read()
            if self.updateText is not None:
                self.updateText(str(res), strategy.key)

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
