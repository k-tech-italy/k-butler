from unittest.mock import Mock

import pytest
from PyQt6.QtWidgets import QGroupBox, QPushButton, QTextEdit


@pytest.fixture
def mock_file_bo(mock_strategy):
    class MockFileBo:
        def __init__(self, file_path):
            self.file_path = file_path
            self.handlers = [mock_strategy]
            self.name = 'Mock file bo'

    yield MockFileBo


@pytest.fixture
def mock_configurator():
    class MockConfigurator:
        name = 'Mock configurator'
        key = 'mock-configurator'

        def get_config(self, action):
            return {'test': 'test'}

    yield MockConfigurator


@pytest.fixture
def mock_strategy(mock_configurator):
    class MockStrategy:
        name = 'Mock strategy'
        key = 'mock'
        actions = {'test action': 'test action'}
        configurator = mock_configurator

        def match(self, file_bo):
            return True

        def get_action(self, action, file_bo):
            assert action == 'test'
            assert file_bo is not None

    yield MockStrategy


def test_text_edit(qtbot):
    from k_butler.components.common import GuiTextEdit
    window = GuiTextEdit('Hello')
    qtbot.addWidget(window)
    window.show()

    assert window.toPlainText() == 'Hello'


def test_modal(qtbot, monkeypatch):
    """Test the GuiModal class."""
    from k_butler.components.common import GuiModal

    monkeypatch.setattr('k_butler.components.common.GuiModal._open_modal', lambda *args: None)

    modal = GuiModal('title', 'test message')
    qtbot.addWidget(modal)
    assert modal.text() == 'test message'


def test_accordion_config_strategy(qtbot, mock_strategy, monkeypatch):
    """Test the GuiAccordion class with config strategy."""
    from k_butler.components.common import GuiAccordion

    mock_read_config = Mock()
    monkeypatch.setattr('k_butler.components.common.GuiAccordion._read_config', mock_read_config)

    strategies = {mock_strategy.key: mock_strategy}
    accordion_widget = GuiAccordion(strategies=strategies)
    qtbot.addWidget(accordion_widget)
    accordion_widget.show()

    config_container = accordion_widget.findChild(QGroupBox)
    assert config_container.title() == 'Mock configurator'

    config_button = config_container.findChild(QPushButton)
    assert config_button.text() == 'Configuration'

    config_button.click()
    assert mock_read_config.call_count == 1


def test_accordion_file_bo(qtbot, mock_file_bo, monkeypatch):
    """Test the GuiAccordion class with files business object."""
    from k_butler.components.common import GuiAccordion

    files_bo = [mock_file_bo('file1'), mock_file_bo('file2')]

    accordion_widget = GuiAccordion(files_bo=files_bo)
    qtbot.addWidget(accordion_widget)
    accordion_widget.show()

    file_container = accordion_widget.findChild(QGroupBox)
    assert file_container.title() == 'Actions'

    action_button = file_container.findChild(QPushButton)
    assert action_button.text() == 'test action'


