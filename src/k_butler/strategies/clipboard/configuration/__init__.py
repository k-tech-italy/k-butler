from k_butler.configuration import ConfigStorage
from k_butler.configuration.base_configurator import StrategyBaseConfigurator


class DrawioCreateTableConfigurator(StrategyBaseConfigurator):
    name = 'Drawio SQL Create Table parser for ERD'
    key = 'drawio_parse'



    @classmethod
    def get_storage(cls):
        return ConfigStorage(strategy_key=cls.key)
