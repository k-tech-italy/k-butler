import yaml
from PyQt6.QtCore import QMargins
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QTabWidget, QPushButton

from k_butler.components.common import GuiTextEdit, GuiModal
from k_butler.strategies.base import Registry


def create_accordion_item(category: str = None):
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

        """files strategy tab"""
        content = TabContent(category='files')
        self.tab.addTab(content, 'Files')

        """clipboard strategy tab"""
        content = TabContent(category='clipboard')
        self.tab.addTab(content, 'Clipboard')

        """config strategy tab"""
        config_strategy_tab = QWidget()
        config_strategy_layout = QVBoxLayout()
        config_strategy_layout.addWidget(self.editor)
        config_strategy_tab.setLayout(config_strategy_layout)
        self.tab.addTab(config_strategy_tab, 'Config')

        main_layout.addWidget(self.tab, 0, 0, 2, 1)


class TabContent(QWidget):
    def __init__(self, category: str, *args, **kwargs):
        """Initializes the TabContent widget."""
        super().__init__(*args, **kwargs)
        self.current_strategy = None
        self.setLayout(QVBoxLayout(self))
        self.strategy = None
        layout = self.layout()

        accordion_items = create_accordion_item(category)

        self.config_editor = ConfigEditor(self.strategy)

        actions_group = QWidget()
        actions_layout = QGridLayout(actions_group)
        actions_layout.setContentsMargins(QMargins(0, 0, 0, 0))

        self.strategy_accordion = ListButton(accordion_items, self.config_editor.update_config)

        actions_layout.addWidget(self.strategy_accordion, 0, 0)
        actions_layout.addWidget(self.config_editor, 1, 1)
        actions_layout.addWidget(self.config_editor, 0, 1)

        layout.addWidget(actions_group)

    def update_strategy(self, *args, **kwargs):
        self.config_editor.update_config(*args, **kwargs)
        self.current_strategy = kwargs['strategy']
        self.config_editor.strategy = self.current_strategy


class ListButton(QWidget):
    def __init__(self, items: dict, on_click_button, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.print = None
        layout = QVBoxLayout()
        for item in items:
            button = QPushButton(item)
            button.setDefault(False)
            button.clicked.connect(lambda checked, i=item: handle_click(items[i]))
            layout.addWidget(button)
        self.setLayout(layout)

        def handle_click(strategy):
            for b in self.findChildren(QPushButton):
                b.setDefault(False) if b.text() != strategy.configurator.name else b.setDefault(True)
            on_click_button(strategy=strategy)


class ConfigEditor(QWidget):
    def __init__(self, strategy=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout()

        self.strategy = strategy
        """config editor"""
        self.config_editor = GuiTextEdit()
        self.config_editor.setReadOnly(True)
        self.config_editor.setPlaceholderText('Select a strategy to configure')

        """save button"""
        self.save_config_button = QPushButton('Save Config')
        self.save_config_button.setDefault(True)
        self.save_config_button.setToolTip('Select a strategy to configure')
        self.save_config_button.clicked.connect(self.save_config)

        if self.strategy is None:
            self.config_editor.setPlaceholderText('No strategies to configure')
            self.save_config_button.setVisible(False)

        layout.addWidget(self.config_editor)
        layout.addWidget(self.save_config_button)
        self.setLayout(layout)

    def save_config(self):
        text = self.config_editor.toPlainText()
        if self.strategy:
            try:
                validated_yaml = yaml.safe_load(text)
                self.strategy.configurator.write_config(validated_yaml)
                self.update_config(strategy=self.strategy)
                GuiModal('success', 'Config saved')
            except Exception as e:
                GuiModal('error', str(e))
        else:
            GuiModal('warning', 'Select one strategy to configure')

    def update_config(self, *args, **kwargs):

        self.save_config_button.setVisible(True)
        self.save_config_button.setDisabled(False)
        self.save_config_button.setToolTip('Save')
        self.config_editor.setReadOnly(False)

        self.strategy = kwargs['strategy']
        config, is_example = self.strategy.configurator.configure()
        if not config or is_example:
            GuiModal('warning', 'There is no Config, you are using the autogenerated one')
        parse_data = yaml.dump(config, default_flow_style=False)
        self.config_editor.setText(parse_data)
