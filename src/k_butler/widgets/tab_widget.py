from PyQt6.QtWidgets import QPushButton, QTabWidget, QVBoxLayout, QWidget

from k_butler.tabs.files import FileSelect


class TabWidget(QTabWidget):

    def __init__(self, parent=...):
        super().__init__(parent)

        self.loadTab(FileSelect)

    def loadTab(self, widget_klass: type[QWidget]):
        widget = widget_klass(self)
        self.addTab(widget, widget.get_label())
        # if tab_widget.children:
        #     ...
