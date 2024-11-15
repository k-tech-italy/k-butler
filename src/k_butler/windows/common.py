from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QSplitter, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget

from k_butler.filesbo import FileBo


class AnotherWindowBase(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, filebo: FileBo):
        super().__init__()
        self.setWindowTitle(filebo.name)

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel(filebo.path))

        splitter = QSplitter(Qt.Orientation.Horizontal)

        tree = QTreeWidget()

        tree.setHeaderLabels(['Actions'])
        tree.addTopLevelItem(QTreeWidgetItem(['One']))
        tree.addTopLevelItem(QTreeWidgetItem(['Two']))

        splitter.addWidget(tree)
        splitter.addWidget(QLabel('Right'))
        splitter.setSizes([100, 200])

        v_layout.addWidget(splitter)

        self.setLayout(v_layout)


def make_window(title):
    from k_butler.controller import controller
    return controller.get_or_create_window(title)
