from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6.QtWidgets import QFileDialog, QLabel, QPushButton, QTabWidget, QVBoxLayout, QWidget, QDialog, QMessageBox

from k_butler.controller import controller
from k_butler.filesbo import FileBo

ADD_FILES = 'Add file(s)'


class FileSelect(QWidget):
    tabLabel = 'Select File'

    def get_label(self):
        return self.tabLabel

    def __init__(self, parent=..., *args):
        super().__init__(parent, *args)

        self.button = QPushButton(ADD_FILES)
        self.setAcceptDrops(True)
        self.setMinimumHeight(100)
        self.setMinimumWidth(400)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.button.clicked.connect(self.open_dialog)

        self.setLayout(layout)

    def dragEnterEvent(self, event, QDragEnterEvent=None):  # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, a0: Optional[QDragEnterEvent]) """
        if event.mimeData().hasUrls():
            self.button.setText("Drop file(s) here")
            event.accept()
        else:
            event.ignore()

    def dragLeaveEvent(self, a0, QDragLeaveEvent=None):  # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) """
        self.button.setText(ADD_FILES)

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]

        self.handle_files(files)

    @pyqtSlot()
    def open_dialog(self):
        fnames = QFileDialog.getOpenFileNames(
            self,
            "Open File(s)",
            "",  # eg. ${HOME}
            "All Files (*);; Excel (*.xlsx);; Calc (*.ods)",
        )
        self.handle_files(fnames[0])

    def handle_files(self, files: list[str]) -> None:
        files_bo = []
        for f in files:
            files_bo.append(FileBo(f))
        controller.get_or_create_window(files_bo)
