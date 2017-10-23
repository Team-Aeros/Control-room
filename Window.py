import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)


        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
