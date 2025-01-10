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

    items = {mock_strategy.configurator.name: mock_strategy}
    accordion_widget = GuiAccordion(items, lambda *args: None, is_config=True)
    qtbot.addWidget(accordion_widget)
    accordion_widget.show()

    config_container = accordion_widget.findChild(QGroupBox)
    config_button = config_container.findChild(QPushButton)
    assert config_button.text() == 'test'


def test_accordion_strategy(qtbot, mock_strategy, monkeypatch):
    """Test the GuiAccordion class with strategy."""
    from k_butler.components.common import GuiAccordion

    items = {mock_strategy.name: mock_strategy}
    accordion_widget = GuiAccordion(items, lambda *args: None)
    qtbot.addWidget(accordion_widget)
    accordion_widget.show()

    strategy_container = accordion_widget.findChild(QGroupBox)
    strategy_button = strategy_container.findChild(QPushButton)
    assert strategy_button.text() == 'test action'
