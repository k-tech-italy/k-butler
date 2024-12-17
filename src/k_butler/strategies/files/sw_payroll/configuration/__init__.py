from k_butler.strategies.base import StrategyBaseConfigurator


class SwPayrollConfigurator(StrategyBaseConfigurator):
    name = 'Singlewave Payroll configurator'
    actions = {
        'split': 'docs/split.txt',
    }

    def split(self):
        pass

    def get_action(self, action: str, file_bo=None):
        action = getattr(self, action)
        action()
