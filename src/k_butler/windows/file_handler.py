from typing import List

from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QGridLayout, QGroupBox, QHBoxLayout, QPushButton, QTextEdit

from k_butler.components.common import GuiAccordion
from k_butler.filesbo import FileBo
from k_butler.tabs.config.components.components import ConfigEditor


class AnotherWindowBase(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, files_bo: List[FileBo]):

        super().__init__()
        self.setWindowTitle('K-Butler')
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)
        self.files_bo = files_bo
        self.is_single_file = len(files_bo) == 1
        self.title_label = "Single file" if self.is_single_file else "Multiple files"
        self.label = QLabel('')

        items = self.create_accordion_item()
        component = QGroupBox('content')
        layout = QGridLayout()

        self.action_detail = ActionDetail(files_bo=self.files_bo)
        self.accordion = GuiAccordion(items, self.action_detail.change_action)
        layout.addWidget(self.accordion, 1, 1)
        layout.addWidget(self.action_detail, 1, 2)

        component.setLayout(layout)

        top_layout = self.create_top_layout()

        main_layout = QVBoxLayout()
        main_layout.addWidget(top_layout)
        main_layout.addWidget(component)
        self.setLayout(main_layout)

    def create_top_layout(self):
        component = QGroupBox(self.title_label)
        layout = QGridLayout()
        for i in range(len(self.files_bo)):  # Add list of files
            layout.addWidget(QLabel(self.files_bo[i].name), i + 1, 0)

        component.setLayout(layout)
        return component

    def create_accordion_item(self):
        accordion_item = {}
        for file_bo in self.files_bo:
            for handler in file_bo.handlers:
                accordion_item[handler.name] = handler
        return accordion_item


class ActionDetail(QGroupBox):
    def __init__(self, files_bo: List[FileBo] = None):
        """
        Action detail widget showing the title of the action and a button to trigger it.
        """
        super().__init__()

        self.action_button = None
        self.description = QTextEdit('')
        self.current_action = None
        self.current_strategy = None

        self.files_bo = files_bo
        self.setMaximumWidth(300)
        self.setMinimumWidth(300)

        h_layout = QHBoxLayout()
        v_layout_detail = QVBoxLayout()

        self.detail = QWidget()
        self.detail.setLayout(QVBoxLayout())
        v_layout_detail.addWidget(self.detail)

        v_layout_detail.addStretch(1)
        h_layout.addLayout(v_layout_detail)
        h_layout.addStretch()

        self.setLayout(h_layout)

    def create_detail_widget(self):
        """Create a detail widget for the given action."""
        if self.current_action == 'configure':
            self._clear_detail_widget()
            config_editor = ConfigEditor(strategy=self.current_strategy)
            self.detail.layout().addWidget(config_editor)
        else:
            self._clear_detail_widget()
            container = QWidget()
            container.setLayout(QVBoxLayout())

            self.action_button = QPushButton()
            self.action_button.clicked.connect(self._get_action)

            self.description.setReadOnly(True)
            self.description.setStyleSheet("background-color: transparent;")
            container.layout().addWidget(self.description)
            container.layout().addWidget(self.action_button)

            self.detail.layout().addWidget(container)

    def _clear_detail_widget(self):
        """Remove all widgets from the detail widget."""
        while self.detail.layout().count():
            child = self.detail.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.action_button = None
        self.description = QTextEdit('')

    def change_action(self, action: str, strategy):  # TODO Manage n files

        self.current_strategy = strategy
        self.current_action = action

        self.create_detail_widget()
        if action != 'configure':
            self.action_button.setText(action)
            self.action_button.setVisible(True)
            self.action_button.setDefault(True)
            description = strategy.get_action_description(action).read_text()
            self.description.setPlainText(description)

    def _get_action(self):
        self.current_strategy.get_action(action=self.current_action, file_bo=self.files_bo[0])


def make_window(title):
    from k_butler.controller import controller
    return controller.get_or_create_window(title)
