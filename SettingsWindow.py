from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5 import QtWidgets
import sys

class SettingsWindow(QWidget):
    def __init__(self):
        layout = QtWidgets.QFormLayout(self)
        minLight = QtWidgets.QLineEdit(self)
        minTemp = QtWidgets.QLineEdit(self)

        chgMinLight = QtWidgets.QPushButton(self)
        chgMinLight.setText("Change the min light value")

        chgMinTemp = QtWidgets.QPushButton(self)
        chgMinTemp.setText("Change the min temp value")

        layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, minLight)
        layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, minTemp)
        layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, chgMinLight)
        layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, chgMinTemp)

    def getLayout(self):
        return self.layout
