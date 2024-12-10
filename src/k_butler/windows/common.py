from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QSplitter, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, QTabWidget, \
    QPushButton, QToolBox, QTextEdit, QPlainTextEdit, QTextBrowser, QGridLayout, QGroupBox, QHBoxLayout

from k_butler.filesbo import FileBo


def create_buttons_actions(strategy):
    result = QGroupBox("Actions")
    button_layout = QVBoxLayout()

    for action in strategy.actions.keys():
        res = QPushButton(action)
        res.setDefault(True)
        button_layout.addWidget(res)

    button_layout.addStretch(1)
    main_layout = QHBoxLayout(result)
    main_layout.addLayout(button_layout)
    main_layout.addStretch()
    return result


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

    def __init__(self, filebo: FileBo):
        super().__init__()
        self.setWindowTitle(filebo.name)
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)
        self.filebo = filebo
        title_label = QLabel("Single file Page")

        top_layout = QHBoxLayout()
        top_layout.addWidget(title_label)

        main_layout = QGridLayout(self)

        strategy_toolbox = self.create_strategy_toolbox()
        strategy_result = create_strategy_result()
        main_layout.addLayout(top_layout, 0, 0, 1, 2)
        main_layout.addWidget(strategy_toolbox, 1, 0)
        main_layout.addWidget(strategy_result, 1, 1)

    def create_strategy_toolbox(self):
        component = QToolBox()
        for handler in self.filebo.handlers:
            component.addItem(create_buttons_actions(handler), handler.name)
            component.addItem(create_buttons_actions(handler), 'test')  # TODO remove this, only for show component
        return component


def make_window(title):
    from k_butler.controller import controller
    return controller.get_or_create_window(title)
