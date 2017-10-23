import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Dashboard(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Dashboard'
        self.left = 10
        self.top = 10
        self.width = 1080
        self.height = 720
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Devices")
        layout = QGridLayout()

        layout.addWidget(QPushButton('Rolluik 1'), 0, 0)
        layout.addWidget(QPushButton('Rolluik 2'), 0, 1)

        self.horizontalGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dashboard()
    sys.exit(app.exec_())