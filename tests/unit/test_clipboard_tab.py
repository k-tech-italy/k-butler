import sys
from unittest.mock import Mock

import pytest
from contextlib import nullcontext as does_not_raise

import pyperclip
from PyQt6.QtWidgets import QApplication, QTabWidget

from k_butler.tabs.clipboard import Clipboard

app = QApplication(sys.argv)
main = QTabWidget()


def test_editor_initialized_with_text():
    pyperclip.copy('test')
    clipboard = Clipboard(main)
    assert clipboard.editor.toPlainText() == 'test'


@pytest.mark.parametrize(
    'text, exception', [
        pytest.param('CREATE TABLE test', does_not_raise(), id='success'),
        pytest.param('error', pytest.raises(
            Exception
        ), id='failed')
    ]
)
def test_text_parsed(monkeypatch, text, exception):
    pyperclip.copy(text)
    clipboard = Clipboard(main)
    error_modal = Mock()
    monkeypatch.setattr('k_butler.components.common.GuiModal._open_modal', error_modal)

    with exception:
        try:
            clipboard.action_clipboard(action='parse')
        except Exception as e:
            assert str(e) == "Text does not start with 'CREATE TABLE '"
            assert error_modal.call_count == 1
        assert clipboard.editor.toPlainText() == 'CREATE TABLE test_1'
