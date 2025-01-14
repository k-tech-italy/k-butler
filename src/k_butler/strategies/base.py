from pathlib import Path
from inspect import getmodule

from k_butler.configuration.base_configurator import StrategyBaseConfigurator
from k_butler.strategies.base_validator import StrategyBaseValidator


class StrategyBase:
    """global base class for all strategies"""
    actions = {}
    configurator = StrategyBaseConfigurator
    validator = StrategyBaseValidator

    @classmethod
    def get_doc_root(cls) -> str:
        return Path(getmodule(cls).__file__).parent

    @classmethod
    def get_action_description(cls, action: str) -> str:
        return cls.get_doc_root() / cls.actions[action]
