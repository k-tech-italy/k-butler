from PyQt6.QtWidgets import QMessageBox, QTextEdit, QToolBox, QGroupBox, QVBoxLayout, QPushButton, QHBoxLayout


def create_error_modal(name, error_message='generic error'):
    modal = QMessageBox()
    modal.setWindowTitle(error_message)
    modal.setText(f"{error_message} {name}")
    modal.setModal(True)
    modal.exec()


class KTTextEdit(QTextEdit):

    def __init__(self, text='', ):
        super().__init__()
        self.setReadOnly(False)
        self.setPlainText(text)

    def setPlainText(self, text):
        super().setPlainText(text)


class KTStrategyAccordion(QToolBox):
    def __init__(self, update_action_detail, files_bo=None, configurator=None):
        """
        Creates a QToolBox widget populated with action buttons.
        Single File = each action button for each strategy
        Multiple Files = Group action for group strategy
        """
        super().__init__()

        if configurator is not None:
            self.addItem(self.create_buttons_actions(configurator, update_action_detail), configurator.name)

        if files_bo is not None:
            self.file_bos = files_bo
            for file_bo in self.file_bos:
                for handler in file_bo.handlers:
                    self.addItem(self.create_buttons_actions(handler,file_bo, update_action_detail), handler.name)

    def create_buttons_actions(self, strategy, file_bo=None, update_action_detail=None):#TODO manage multiple files
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
