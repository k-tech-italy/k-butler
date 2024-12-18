def test_text_edit(qtbot):
    from k_butler.components.common import GuiTextEdit
    window = GuiTextEdit('Hello')
    qtbot.addWidget(window)
    window.show()

    assert window.toPlainText() == 'Hello'


def test_modal(qtbot):
    from k_butler.components.common import GuiModal
    modal = GuiModal('this is a message:', 'for test')
    qtbot.addWidget(modal)
    modal.show()

    assert modal.text() == 'this is a message: for test'
