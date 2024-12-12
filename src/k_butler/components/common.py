from PyQt6.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox


def create_buttons_actions(files_bo, strategy):
    # TODO Generalize input props
    result = QGroupBox("Actions")
    button_layout = QVBoxLayout()

    for action in strategy.actions.keys():
        button = QPushButton(action)
        button.setDefault(True)
        button.clicked.connect(lambda checked, a=action, f=files_bo[0]: strategy.get_action(a, f))

        button_layout.addWidget(button)

    button_layout.addStretch(1)
    main_layout = QHBoxLayout(result)
    main_layout.addLayout(button_layout)
    main_layout.addStretch()
    return result


def create_error_modal(name, error_message='generic error'):
    modal = QMessageBox()
    modal.setWindowTitle(error_message)
    modal.setText(f"{error_message} {name}")
    modal.setModal(True)
    modal.exec()
