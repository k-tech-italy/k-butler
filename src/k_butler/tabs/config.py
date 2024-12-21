from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

from k_butler.components.common import GuiTextEdit, GuiAccordion, GuiModal
from k_butler.configuration import ConfigStorage
from k_butler.strategies.base import Registry
import ast


class ConfigTab(QWidget):
    tabLabel = 'Payroll Config'

    def __init__(self, parent=..., *args):
        super().__init__(parent, *args)
        main_layout = QVBoxLayout()
        self.editor = GuiTextEdit()
        self.current_strategy = None

        strategies = Registry().strategies
        save_config_button = QPushButton('Save Config')
        save_config_button.setDefault(True)
        save_config_button.clicked.connect(lambda: self.validate_dict(self.editor.toPlainText()))

        action_layout = QGroupBox('Actions')
        layout = QGridLayout()
        strategy_toolbox = GuiAccordion(self.update_text, strategies=strategies, is_config=True)

        layout.addWidget(strategy_toolbox, 1, 1)
        layout.addWidget(save_config_button, 2, 2)
        layout.addWidget(self.editor, 1, 2)

        action_layout.setLayout(layout)
        main_layout.addWidget(action_layout)
        self.setLayout(main_layout)

    def update_action_detail(self, action):
        pass

    def update_text(self, text, strategy):
        self.current_strategy = strategy
        self.editor.setText(text)

    def validate_dict(self, text):
        config_storage = ConfigStorage(self.current_strategy)
        try:
            res = ast.literal_eval(text)
            config_storage.write(res)
            updated_text = config_storage.read()
            self.editor.setText(str(updated_text))

        except Exception as e:
            GuiModal('error', str(e))
