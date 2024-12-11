from k_butler.filesbo import FileBo
from k_butler.strategies.base import register, StrategyBaseConfigurator
from PyPDF2 import PdfReader, PdfWriter
from PyQt6.QtCore import pyqtSlot


class SwPayrollConfigurator(StrategyBaseConfigurator):
    pass


@register
class SwPayrollStrategy:
    name = 'Singlewave Payroll processor'
    description = 'Single wave payroll processor strategy.'
    actions = {
        'split': 'docs/split.txt',
        'configure': 'Configure payroll',
    }
    configurator = SwPayrollConfigurator()

    def match(self, file_bo: FileBo) -> bool:
        if not file_bo.name.endswith(".pdf"):
            return False
        else:
            file_bo.add_handler(self)
            return True

    @pyqtSlot()
    def split(self, file_bo: FileBo):
        #TODO use Tmp folder

        input_pdf = PdfReader(file_bo.fullpath.__str__())
        for page_num, page in enumerate(input_pdf.pages, 1):
            writer = PdfWriter()
            writer.add_page(page)
            writer.write(file_bo.name)
            single_page = open(f'{file_bo.name}_{page_num}.pdf', 'wb')
            writer.write(single_page)
            single_page.close()
            writer.close()

    @pyqtSlot()
    def configure(self, file_bo: FileBo):
        pass

    @pyqtSlot()
    def get_action(self, action: str, file_bo: FileBo):
        action = getattr(self, action)
        action(file_bo)
