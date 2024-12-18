from typing import List

from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QToolBox, QGridLayout, QGroupBox, QHBoxLayout, QPushButton

from k_butler.components.common import GuiAccordion
from k_butler.filesbo import FileBo


class AnotherWindowBase(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, files_bo: List[FileBo]):
        super().__init__()
        self.action_detail = None
        self.setWindowTitle('K-Butler')
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)
        self.files_bo = files_bo
        single_file = len(files_bo) == 1
        self.title_label = "Single file Page" if single_file else "Multiple files Page"
        self.label = QLabel('')
        content = self.create_content_layout()

        top_layout = self.create_top_layout()

        main_layout = QVBoxLayout()
        main_layout.addWidget(top_layout)
        main_layout.addWidget(content)
        self.setLayout(main_layout)

    def create_top_layout(self):
        component = QGroupBox(self.title_label)
        layout = QGridLayout()
        for i in range(len(self.files_bo)):  # Add list of files
            layout.addWidget(QLabel(self.files_bo[i].name), i + 1, 0)

        component.setLayout(layout)
        return component

    def create_strategy_toolbox(self):
        """
        Creates a QToolBox widget populated with action buttons.
        Single File = each action button for each strategy
        Multiple Files = Group action for group strategy
        """
        component = QToolBox()  # TODO add group strategy
        for f in self.files_bo:
            for handler in f.handlers:
                component.addItem(self.create_buttons_actions(handler), handler.name)
            return component

    def create_content_layout(self):
        """
        Creates layout grid for components
        """
        component = QGroupBox('content')
        layout = QGridLayout()
        strategy_toolbox = GuiAccordion(files_bo=self.files_bo)
        self.action_detail = self.create_action_detail()

        layout.addWidget(strategy_toolbox, 1, 1)
        layout.addWidget(self.action_detail, 1, 2)

        component.setLayout(layout)
        return component

    def create_buttons_actions(self, strategy):

        buttons_component = QGroupBox("Actions")
        button_layout = QVBoxLayout()

        for action in strategy.actions.keys():
            button = QPushButton(action)
            button.setDefault(True)
            # button.clicked.connect(lambda checked, a=action, f=self.files_bo[0]: strategy.get_action(a, f))
            button.clicked.connect(lambda checked, a=action: self.update_action_detail(a))
            button_layout.addWidget(button)

        button_layout.addStretch(1)
        main_layout = QHBoxLayout(buttons_component)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        return buttons_component

    def update_action_detail(self, action):
        self.label.setText(f'{action}')

    def create_action_detail(self):

        result = QGroupBox("Action details")
        self.label = QLabel("Select an action")

        h_layout = QHBoxLayout(result)
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.label)
        v_layout.addStretch(1)

        button = QPushButton(self.label)
        button.setDefault(True)
        #button.clicked.connect(lambda checked, a=self.label, f=self.files_bo[0]: strategy.get_action(a, f))
        v_layout.addWidget(button)

        h_layout.addLayout(v_layout)
        h_layout.addStretch()

        return result


def make_window(title):
    from k_butler.controller import controller
    return controller.get_or_create_window(title)
