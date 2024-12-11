from PyQt6.QtWidgets import QWidget, QGridLayout, QTabWidget

from k_butler.tabs.clipboard import Clipboard
from k_butler.tabs.core import FileSelect


class TabsWidget(QWidget):

    def __init__(self, *args, **kwargs):
        """
        Initializes the TabsWidget and adding n single TabWidget to it.
        """
        super().__init__(*args, **kwargs)

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        tab = QTabWidget(self)

        file_page = FileSelect(self)
        clipboard_page = Clipboard(self)

        tab.addTab(file_page, file_page.tabLabel)
        tab.addTab(clipboard_page, clipboard_page.tabLabel)

        main_layout.addWidget(tab, 0, 0, 2, 1)
