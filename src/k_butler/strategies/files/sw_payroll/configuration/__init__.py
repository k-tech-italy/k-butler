from k_butler.configuration import ConfigStorage
from k_butler.strategies.base import StrategyBaseConfigurator


def get_config(action: str):
    return ConfigStorage(action).read()


class SwPayrollConfigurator(StrategyBaseConfigurator):
    name = 'Singlewave Payroll configurator'
    key = 'sw_payroll'
    actions = {
        'configure': 'configure payroll',
    }

    def __init__(self):
        super().__init__()
        self.storage = ConfigStorage(self.key)

    def configure(self):
        res = self.storage.read()
        controller
        return res
