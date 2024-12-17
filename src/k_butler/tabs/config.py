from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout

from k_butler.components.common import KTTextEdit, KTStrategyAccordion
from k_butler.strategies.files.sw_payroll.sw_payroll import SwPayrollStrategy


class ConfigTab(QWidget):
    tabLabel = 'Payroll Config'
    strategy = SwPayrollStrategy

    def __init__(self, parent=..., *args):
        super().__init__(parent, *args)
        main_layout = QVBoxLayout()
        self.editor = KTTextEdit()

        action_layout = QGroupBox('Actions')
        layout = QGridLayout()
        strategy_toolbox = KTStrategyAccordion(self.update_action_detail, configurator=self.strategy.configurator)

        layout.addWidget(strategy_toolbox, 1, 1)
        layout.addWidget(self.editor, 1, 2)

        action_layout.setLayout(layout)
        main_layout.addWidget(action_layout)
        self.setLayout(main_layout)

    def update_action_detail(self, action):
        pass
