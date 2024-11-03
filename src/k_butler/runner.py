import sys

from k_butler import __version__, strategies

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, QMainWindow,
                             QPushButton, QTabWidget, QTextEdit, QVBoxLayout, QWidget, )

from k_butler.strategies.base import Registry
from k_butler.styles.tabs import CustomTabStyle

FILESTORE = '.'


class Store:
    _filestore = None

    def __init__(self):
        if self._filestore is None:
            pass


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        Registry().load()

        self.setWindowTitle(f"K-Butler ({__version__})")

        tabWidget = QtWidgets.QTabWidget()
        self.setCentralWidget(tabWidget)
        tabWidget.setStyle(CustomTabStyle())
        tabWidget.setTabPosition(QTabWidget.TabPosition.West)

        tab1 = QWidget()
        tab2 = QWidget()

        tab1.setLayout(layout := QVBoxLayout())
        layout.addWidget(QLabel("Drag a file or click to select"))

        tab2.setLayout(layout := QVBoxLayout())
        layout.addWidget(QPushButton("PyQt5 button"))

        tabWidget.addTab(tab1, 'Select File')
        tabWidget.addTab(tab2, 'Settings')

        #
        #
        #
        #
        # self.setAcceptDrops(True)
        #
        # vLayout = QVBoxLayout()
        # hLayout = QHBoxLayout()
        #
        # self.pathLE = QtWidgets.QLabel(self)
        # hLayout.addWidget(self.pathLE)
        # self.loadBtn = QtWidgets.QPushButton("Select File(s)", self)
        # hLayout.addWidget(self.loadBtn)
        # vLayout.addLayout(hLayout)
        #
        # # self.filesTv = QtWidgets.QTableView(self)
        # # vLayout.addWidget(self.filesTv)
        # # self.filesTv.setSortingEnabled(True)
        #
        # self.show_actions()
        #
        #
        # self.loadBtn.clicked.connect(self.load_file)
        #
        # widget = QWidget()
        # widget.setLayout(vLayout)
        # self.setCentralWidget(widget)

    def dragEnterEvent(self, event):
        print('dragEnterEvent')
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        print('dropEvent')
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)

    def load_file(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open File",
            ".data/sw-payroll/tmp",
            "PDF Files (*.pdf);; Excel Files (*.xlsx);; CSV Files (*.csv);; ZIP Files (*.zip);; All files (*.*)"
        )
        if filename:
            suffix = filename.split(".")[-1]

            self.pathLE.setText(filename)

            if not filename.endswith(".pdf"):
                self.pathLE.setText(f'Cannot handle yet suffix {suffix}')
                return

            for strategy_name, strategy in Registry().strategies.items():
                if strategy().match(filename):
                    self.pathLE.setText(f'Matched strategy {strategy_name}')

            #
            #
            # df = load_df(filename)
            # df = apply_rules(df)
            #
            # model = DataFrameModel(df)
            # self.filesTv.setModel(model)
            #
            # filename = Path(filename)
            # output = filename.parent / f'out_{filename.name}'
            # df.to_csv(output, index=False)

    def show_actions(self):
        self.tabActionsWidget = QtWidgets.QTabWidget(self)
        self.tabActionsWidget.tabPosition()
        self.tabActionsWidget.setStyle(CustomTabStyle())

        self.tabActions = {
            'Select File': (tab1 := QWidget()),
            'Settings': (tab2 := QWidget())
        }

        tab1.layout = QVBoxLayout(self)
        pushButton1 = QPushButton("PyQt5 button")
        tab1.layout.addWidget(pushButton1)
        tab1.setLayout(tab1.layout)

        for k, v in self.tabActions.items():
            self.tabActionsWidget.addTab(v, k)
        self.tabActionsWidget.resize(300, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_gui = Main()
    main_gui.show()
    sys.exit(app.exec())
