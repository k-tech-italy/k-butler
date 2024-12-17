import tempfile
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter
from PyQt6.QtCore import pyqtSlot

from k_butler.filesbo import FileBo
from k_butler.strategies.base import register
from k_butler.strategies.files.sw_payroll.configuration import SwPayrollConfigurator
from k_butler.strategies.utils import open_file


@register
class SwPayrollStrategy:
    name = 'Singlewave Payroll processor'
    key = 'sw_payroll'
    description = 'Single wave payroll processor strategy.'
    actions = {
        'split': 'docs/split.txt',
        'configure': 'Configure payroll',
    }
    configurator = SwPayrollConfigurator

    def match(self, file_bo: FileBo) -> bool:
        if not file_bo.name.endswith(".pdf"):
            return False
        else:
            file_bo.add_handler(self)
            return True

    @pyqtSlot()
    def split(self, file_bo: FileBo):
        """Split a PDF file into multiple PDFs, one per page."""

        with tempfile.TemporaryDirectory(prefix='sw_payroll', delete=False) as temp_dir:
            input_pdf = PdfReader(str(file_bo.fullpath))
            for page_num, page in enumerate(input_pdf.pages, 1):
                output_filename = f"page_{page_num}.pdf"
                output_path = Path(temp_dir) / output_filename
                with open(output_path, 'wb') as output_file:
                    writer = PdfWriter(output_file)
                    writer.add_page(page)
                    writer.write(output_file)
                    writer.close()

            open_file(Path(temp_dir))

    def configure(self, file_bo: FileBo):
        pass

    def get_action(self, action: str, file_bo: FileBo):
        action = getattr(self, action)
        action(file_bo)
