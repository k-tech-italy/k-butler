from k_butler.configuration import ConfigStorage
from k_butler.configuration.base_configurator import StrategyBaseConfigurator


class KTechPayrollConfigurator(StrategyBaseConfigurator):
    name = 'K-Tech Payroll configurator'
    key = 'kt_payroll'
    actions = {
        'configure': 'configure payroll',
    }

    @classmethod
    def get_storage(cls):
        return ConfigStorage(strategy_key=cls.key)
