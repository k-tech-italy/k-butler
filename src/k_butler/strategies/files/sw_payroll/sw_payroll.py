import tempfile
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter
from pydantic_core._pydantic_core import ValidationError

from k_butler.components.common import GuiModal
from k_butler.filesbo import FileBo
from k_butler.strategies import register
from k_butler.strategies.files.base import FileStrategyBase
from k_butler.strategies.files.sw_payroll.configuration import SwPayrollConfigurator
from k_butler.strategies.files.sw_payroll.validator import SwPayrollValidator
from k_butler.strategies.utils import open_file


@register
class SwPayrollStrategy(FileStrategyBase):
    name = 'Singlewave Payroll processor'
    key = 'sw_payroll'
    description = 'Single wave payroll processor strategy.'
    actions = {
        'split': 'docs/split.txt',
        'configure': 'docs/configure.txt',
    }
    configurator = SwPayrollConfigurator
    validator = SwPayrollValidator

    def match(self, file_bo: FileBo) -> bool:
        """Check if a file matches this strategy."""
        if self.configurator.exist():
            config, _ = self.configurator.configure()
            try:
                self.validator(**config)
            except ValidationError:
                return False
            file_bo.add_handler(self)
            return True


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

    def configure(self, *args, **kwargs):
        from k_butler.controller import controller
        controller.set_main_in_front()

    def get_action(self, *args, **kwargs):
        action = kwargs['action']
        file_bo = kwargs['file_bo']
        action = getattr(self, action)
        action(file_bo)
