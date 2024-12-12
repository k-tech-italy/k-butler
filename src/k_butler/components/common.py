from PyQt6.QtWidgets import QMessageBox


def create_error_modal(name, error_message='generic error'):
    modal = QMessageBox()
    modal.setWindowTitle(error_message)
    modal.setText(f"{error_message} {name}")
    modal.setModal(True)
    modal.exec()
