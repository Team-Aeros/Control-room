import sys
from PyQt5.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QW
from PyQt5.QtGui import *
from PyQt5.QtCore import *


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

        windowLayout = QGridLayout()

        windowLayout.addWidget(self.createGridLayout(), 0, 1)
        windowLayout.addWidget(self.createMenu(),0,0)

        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        Grid = QGroupBox("Devices")
        layout = QGridLayout()

        layout.addWidget(QPushButton('Rolluik 1'), 0, 0)
        layout.addWidget(QPushButton('Rolluik 2'), 0, 1)

        Grid.setLayout(layout)
        return Grid

    def createMenu(self):
        menuBar = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QPushButton("Manual mode"))
        layout.addWidget(QPushButton("Statistics"))

        menuBar.setLayout(layout)
        return menuBar


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dashboard()
    sys.exit(app.exec_())