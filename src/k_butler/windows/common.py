from typing import List

from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QToolBox, QGridLayout, QGroupBox, QHBoxLayout

from k_butler.filesbo import FileBo
from k_butler.components.common import create_buttons_actions


def create_strategy_result():
    result = QGroupBox("Result")
    h_layout = QHBoxLayout(result)
    v_layout = QVBoxLayout()
    v_layout.addWidget(QLabel("Result"))
    v_layout.addStretch(1)

    h_layout.addLayout(v_layout)
    h_layout.addStretch()

    return result


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
        single_file = len(files_bo) == 1
        self.title_label = "Single file Page" if single_file else "Multiple files Page"
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
                component.addItem(create_buttons_actions(self.files_bo, handler), handler.name)
            return component

    def create_content_layout(self):
        """
        Creates layout grid for components
        """
        component = QGroupBox('content')
        layout = QGridLayout()

        strategy_toolbox = self.create_strategy_toolbox()
        strategy_result = create_strategy_result()

        layout.addWidget(strategy_toolbox, 1, 1)
        layout.addWidget(strategy_result, 1, 2)

        component.setLayout(layout)
        return component


def make_window(title):
    from k_butler.controller import controller
    return controller.get_or_create_window(title)
