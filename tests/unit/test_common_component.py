from unittest.mock import Mock

from PyQt6.QtWidgets import QGroupBox, QPushButton


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
    accordion_widget = GuiAccordion(strategies=strategies, is_config=True)
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
