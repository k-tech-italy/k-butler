import inspect
from typing import Dict, Any


class Registry:
    _strategies = {}

    @property
    def strategies(self) -> Dict[str, Any]:
        return self._strategies

    def load(self):
        from k_butler.strategies.clipboard.drawio import DrawioCreateTableParse
        from k_butler.strategies.files.kt_payroll.kt_payroll import KtPayrollStrategy
        from k_butler.strategies.files.sw_payroll.sw_payroll import SwPayrollStrategy

        register(DrawioCreateTableParse)
        register(KtPayrollStrategy)
        register(SwPayrollStrategy)


def register(klass):
    Registry._strategies[klass.key] = klass

    # def wrapper_func():
    #     # Do something before the function.
    #     func()
    #     # Do something after the function.
    return klass
