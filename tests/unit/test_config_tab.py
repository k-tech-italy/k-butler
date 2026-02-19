import sys
from pathlib import Path
from unittest.mock import Mock
import pytest
import yaml
from PyQt6.QtWidgets import QApplication, QTabWidget
from contextlib import nullcontext as does_not_raise

# from k_butler.tabs.config import ConfigTab
#
# app = QApplication(sys.argv)
# main = QTabWidget()
#
#
# def test_editor_initialized_with_text():
#     config = ConfigTab(main)
#     assert config.get_label() == 'Config'
#
#
# @pytest.mark.parametrize(
#     'text, exception', [
#         pytest.param('{"pippo":"pluto"}', does_not_raise(), id='success'),
#         pytest.param('{"pippo":"pluto" errr}', pytest.raises(
#             Exception
#         ), id='failed')
#     ]
# )
# def test_validate_config(monkeypatch, text, exception, mock_strategy):
#     config = ConfigTab(main)
#     config.current_strategy = mock_strategy
#     mock_write = Mock()
#     error_modal = Mock()
#     monkeypatch.setattr('k_butler.configuration.ConfigStorage.write', mock_write)
#     monkeypatch.setattr('k_butler.components.common.GuiModal._open_modal', error_modal)
#     with exception:
#         try:
#             config.validate_dict(text)
#         except Exception:
#             assert error_modal.call_count == 1
#         assert mock_write.call_count == 1
#
#
# def test_update_text(monkeypatch, mock_strategy):
#     config = ConfigTab(main)
#     text = {"pippo": "pluto"}
#     expect = yaml.dump(text, default_flow_style=False)
#     mock_read = Mock(return_value=[text, False])
#     monkeypatch.setattr('k_butler.configuration.ConfigStorage.read', mock_read)
#
#     config.update_text(strategy=mock_strategy)
#     assert mock_read.call_count == 1
#
#     assert config.editor.toPlainText() == expect
