from typing import Any, Dict


class Registry:
    _strategies = {}

    @property
    def strategies(self) -> Dict[str, Any]:
        return self._strategies

    def load(self):
        pass


def register(klass):
    Registry._strategies[klass.name] = klass

    # def wrapper_func():
    #     # Do something before the function.
    #     func()
    #     # Do something after the function.
    return klass


class StrategyBaseConfigurator:
    page = None
