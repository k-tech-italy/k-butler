from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QSplitter, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget

from k_butler.filesbo import FileBo
from k_butler.strategies.base import Registry


class AnotherWindowBase(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, filebo: FileBo):
        super().__init__()
        self.setWindowTitle(filebo.name)
        strategies = Registry().strategies

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel(filebo.path))

        splitter = QSplitter(Qt.Orientation.Horizontal)

        tree = QTreeWidget()

        for title, klass in strategies.items():
            tree.setHeaderLabels([title])
            for action in klass.actions.keys():
                item = QTreeWidgetItem([action])
                tree.addTopLevelItem(item)
                item.setData(0, Qt.ItemDataRole.UserRole, (klass, action))

        tree.itemClicked.connect(self.trigger_action)

        splitter.addWidget(tree)
        splitter.addWidget(QLabel('Right'))
        splitter.setSizes([100, 200])

        v_layout.addWidget(splitter)

        self.setLayout(v_layout)
    def trigger_action(self, item):
        klass, action_name = item.data(0, Qt.ItemDataRole.UserRole)
        action = getattr(klass, action_name, None)
        if callable(action):
            action()


def make_window(title):
    from k_butler.controller import controller
    return controller.get_or_create_window(title)