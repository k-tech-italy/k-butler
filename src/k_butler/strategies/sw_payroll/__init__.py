from typing import Optional, List

from k_butler.filesbo import FileBo
from k_butler.strategies.base import register, StrategyBaseConfigurator


class SwPayrollConfigurator(StrategyBaseConfigurator):
    pass


@register
class SwPayrollStrategy:
    name = 'Singlewave Payroll processor'
    description = 'Single wave payroll processor strategy.'
    actions = {
        'split': 'Just split',
        'configure': 'Configure payroll',
    }
    configurator = SwPayrollConfigurator()

    def match(self, file_bo: FileBo) -> None:
        if file_bo.name.endswith(".pdf"):
            file_bo.add_handler(self)
