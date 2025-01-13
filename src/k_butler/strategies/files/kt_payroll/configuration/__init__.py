from k_butler.configuration import ConfigStorage
from k_butler.strategies.base import StrategyBaseConfigurator


def validate_config(*args, **kwargs) -> bool:
    """do strategy specific validation"""
    return True


class KTechPayrollConfigurator(StrategyBaseConfigurator):
    name = 'K-Tech Payroll configurator'
    key = 'kt_payroll'
    actions = {
        'configure': 'configure payroll',
    }

    @classmethod
    def get_storage(cls):
        return ConfigStorage(strategy_key=cls.key)

    @classmethod
    def configure(cls):
        return cls.get_storage().read()

    @classmethod
    def write_config(cls, config: dict, *args, **kwargs):
        storage = cls.get_storage()
        if validate_config(config):
            storage.write(config)



