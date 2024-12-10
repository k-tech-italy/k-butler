from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QVBoxLayout


class HomePage():

    @classmethod
    def load(mainwindow: QMainWindow):
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()

        hLayout.addWidget(QtWidgets.QLabel(mainwindow))
        self.loadBtn = QtWidgets.QPushButton("Select File(s)", self)
        hLayout.addWidget(self.loadBtn)
        vLayout.addLayout(hLayout)


        # self.filesTv = QtWidgets.QTableView(self)
        # vLayout.addWidget(self.filesTv)
        # self.filesTv.setSortingEnabled(True)

        self.show_actions()


        self.loadBtn.clicked.connect(self.load_file)