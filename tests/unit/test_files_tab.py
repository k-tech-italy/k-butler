import sys
from unittest.mock import Mock
import pathlib

from PyQt6.QtWidgets import QTabWidget, QApplication

from k_butler.tabs.files import FileSelect

app = QApplication(sys.argv)
main = QTabWidget()


# @pytest.fixture
# def mock_drop_event():
#     class MockQUrl:
#         def __init__(self, url):
#             self.url = url
#
#         def toLocalFile(self):
#             return self.url
#
#     class MockMimeData:
#         def __init__(self, urls=None):
#             self.urls = urls if urls else []
#
#         def urls(self):
#             return [MockQUrl(url) for url in self.urls]
#
#     class MockDropEvent:
#         def __init__(self):
#             self.mime_data = MockMimeData()
#
#         def mimeData(self):
#             return MockMimeData()
#
#     yield MockDropEvent

def test_file_select_label():
    file_select = FileSelect(main)
    assert file_select.get_label() == 'Select File'


def test_file_select_handle_files(monkeypatch):
    mock_open_window = Mock()
    monkeypatch.setattr('k_butler.controller.Controller.get_or_create_window', mock_open_window)
    file_select = FileSelect(main)
    path = pathlib.Path('tests/examples/kt_buste_paga/kt_buste_paga.pdf').resolve()
    files = [str(path)]
    file_select.handle_files(files)
    assert mock_open_window.call_count == 1
