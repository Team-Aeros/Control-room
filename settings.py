# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class settingsWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(422, 87)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.minLight = QtWidgets.QLineEdit(Form)
        self.minLight.setObjectName("minLight")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minLight)
        self.chgMinLight = QtWidgets.QPushButton(Form)
        self.chgMinLight.setObjectName("chgMinLight")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chgMinLight)
        self.minTemp = QtWidgets.QLineEdit(Form)
        self.minTemp.setObjectName("minTemp")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.minTemp)
        self.chgMinTemp = QtWidgets.QPushButton(Form)
        self.chgMinTemp.setObjectName("chgMinTemp")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chgMinTemp)
        self.horizontalLayout.addLayout(self.formLayout)

        self.retranslateUi(Form)
        self.chgMinLight.clicked.connect(self.chgMinLightVal)
        self.chgMinTemp.clicked.connect(self.chgMinTempVal)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def chgMinLightVal(self):
        pass

    def chgMinTempVal(self):
        pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Change settings"))
        self.chgMinLight.setText(_translate("Form", "Change Min light value"))
        self.chgMinTemp.setText(_translate("Form", "Change Min temp value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = settingsWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

