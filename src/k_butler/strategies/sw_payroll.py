from typing import Optional

from k_butler.strategies.base import register


def split():
    return 'split'


@register
class SwPayrollProcessor:
    name = 'Singlewave Payroll processor'
    description = 'Single wave payroll processor strategy.'
    actions = {
        'split': 'Just split',
        'configure': 'Configure payroll',
    }
    split = split()

    def match(self, filename) -> Optional[list]:
        return self.actions
