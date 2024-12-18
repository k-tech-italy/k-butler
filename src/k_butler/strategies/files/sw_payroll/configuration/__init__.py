from k_butler.configuration import ConfigStorage
from k_butler.strategies.base import StrategyBaseConfigurator


def get_config(action: str):
    return ConfigStorage(action).read()


class SwPayrollConfigurator(StrategyBaseConfigurator):
    name = 'Singlewave Payroll configurator'

    def split(self):
        pass


