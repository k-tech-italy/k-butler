from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget

class AnotherWindowBase(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, title):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(title)
        layout.addWidget(self.label)
        self.setLayout(layout)


def make_window(title):
    from k_butler.controller import controller
    return controller.get_or_create_window(title)
