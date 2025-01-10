from PyQt6.QtWidgets import QWidget, QGridLayout, QTabWidget

from k_butler.tabs.clipboard import Clipboard
from k_butler.tabs.config import ConfigTab
from k_butler.tabs.files import FileSelect


class TabsWidget(QWidget):

    def __init__(self, *args, **kwargs):
        """
        Initializes the TabsWidget and adding n single TabWidget to it.
        """
        super().__init__(*args, **kwargs)

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        self.tab = QTabWidget(self)

        file_tab = FileSelect(self)
        clipboard_tab = Clipboard(self)
        config_tab = ConfigTab(self)

        self.tab.addTab(file_tab, file_tab.tabLabel)
        self.tab.addTab(clipboard_tab, clipboard_tab.tabLabel)
        self.tab.addTab(config_tab, config_tab.tabLabel)

        main_layout.addWidget(self.tab, 0, 0, 2, 1)
