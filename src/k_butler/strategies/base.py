import inspect
from pathlib import Path
from typing import Any, Dict


class Registry:
    _strategies = {}

    @property
    def strategies(self) -> Dict[str, Any]:
        return self._strategies

    def load(self):
        from k_butler.strategies.files.sw_payroll.sw_payroll import SwPayrollStrategy as _


def register(klass):
    Registry._strategies[klass.key] = klass

    # def wrapper_func():
    #     # Do something before the function.
    #     func()
    #     # Do something after the function.
    return klass


class StrategyBaseConfigurator:
    page = None


    @classmethod
    def get_config_filename(cls) -> str:
        strategy_type = Path(cls.__module__).suffixes[1][1:]
        return f'{strategy_type}/{cls.__name__.lower()}.yaml'


    @classmethod
    def get_example_file(cls) -> Path:
        """Recursively find parent 'configuration' folder and return example file."""
        cursor = Path(inspect.getfile(cls)).parent
        while cursor.name != 'configuration':
            cursor = cursor.parent
        return cursor / 'example.yaml'
