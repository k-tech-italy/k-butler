
class Registry:
    _strategies = {}

    @property
    def strategies(self) -> dict:
        return self._strategies

    def load(self):
        from . import sw_payroll as _


def register(klass):
    Registry._strategies[klass.name] = klass

    # def wrapper_func():
    #     # Do something before the function.
    #     func()
    #     # Do something after the function.
    return klass


