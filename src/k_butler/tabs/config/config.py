from PyQt6.QtCore import QMargins
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QTabWidget

from k_butler.components.common import GuiTextEdit
from k_butler.strategies import Registry
from k_butler.tabs.config.components.components import ConfigEditor, ListButton


def create_accordion_item(category: str = None) -> dict:
    accordion_item = {}
    strategies = Registry().strategies
    filtered_strategies = {k: v for k, v in strategies.items() if v.category == category} if category else strategies
    for strategy in filtered_strategies:
        if strategies[strategy].configurator is not None:
            title = strategies[strategy].configurator.name
            accordion_item[title] = strategies[strategy]
    return accordion_item


class ConfigTab(QWidget):
    tabLabel = 'Config'

    def get_label(self):
        return self.tabLabel

    def __init__(self, parent=..., *args):
        super().__init__(parent, *args)
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        self.editor = GuiTextEdit()
        self.editor.setReadOnly(True)
        self.editor.setPlaceholderText('Select one strategy to configure')
        self.current_strategy = None

        self.tab = QTabWidget(self)
        """config strategy tab"""
        content = TabContent(category='global')
        self.tab.addTab(content, 'Global config')

        """files strategy tab"""
        content = TabContent(category='files')
        self.tab.addTab(content, 'Files')

        """clipboard strategy tab"""
        content = TabContent(category='clipboard')
        self.tab.addTab(content, 'Clipboard')

        main_layout.addWidget(self.tab, 0, 0, 2, 1)


class TabContent(QWidget):
    def __init__(self, category: str, *args, **kwargs):
        """Initializes the TabContent widget."""
        super().__init__(*args, **kwargs)
        self.current_strategy = None
        self.setLayout(QVBoxLayout(self))
        self.strategy = None

        actions_group = QWidget()
        actions_layout = QGridLayout(actions_group)
        actions_layout.setContentsMargins(QMargins(0, 0, 0, 0))

        accordion_items = create_accordion_item(category)
        self.config_editor = ConfigEditor(self.strategy, is_global=category == 'global')
        self.strategy_accordion = ListButton(accordion_items, self.config_editor.update_config)

        actions_layout.addWidget(self.strategy_accordion, 0, 0)
        actions_layout.addWidget(self.config_editor, 0, 1)

        self.layout().addWidget(actions_group)


