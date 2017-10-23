# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 430)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.showDetR1 = QtWidgets.QPushButton(Form)
        self.showDetR1.setMaximumSize(QtCore.QSize(75, 16777215))
        self.showDetR1.setObjectName("showDetR1")
        self.gridLayout.addWidget(self.showDetR1, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setObjectName("quit")
        self.gridLayout.addWidget(self.quit, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Help = QtWidgets.QPushButton(Form)
        self.Help.setObjectName("Help")
        self.gridLayout.addWidget(self.Help, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.printText = QtWidgets.QPushButton(Form)
        self.printText.setMaximumSize(QtCore.QSize(50, 16777215))
        self.printText.setObjectName("printText")
        self.gridLayout.addWidget(self.printText, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        self.printText.clicked.connect(self.print_text)
        self.showDetR1.clicked.connect(self.show_det)
        self.quit.clicked.connect(self.quit_app)
        self.Help.clicked.connect(self.print_help)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dashboard"))
        self.showDetR1.setText(_translate("Form", "Rolluik 1"))
        self.quit.setText(_translate("Form", "Quit"))
        self.Help.setText(_translate("Form", "Help"))
        self.printText.setToolTip(_translate("Form", "<html><head/><body><p>Prints text</p></body></html>"))
        self.printText.setText(_translate("Form", "Print"))

    def print_text(self):
        print("Hello World")

    def show_det(self):
        print("Status:  help")

    def quit_app(self):
        sys.exit(app.exec_())

    def print_help(self):
        print("help not coming for you")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

