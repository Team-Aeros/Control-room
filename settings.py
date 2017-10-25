# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class settingsWindow(object):
    def setupSettingsWindowUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(422, 167)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.minLight = QtWidgets.QLineEdit(Form)
        self.minLight.setObjectName("minLight")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minLight)
        self.maxLight = QtWidgets.QLineEdit(Form)
        self.maxLight.setObjectName("maxLight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxLight)
        self.minTemp = QtWidgets.QLineEdit(Form)
        self.minTemp.setObjectName("minTemp")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.minTemp)
        self.maxTemp = QtWidgets.QLineEdit(Form)
        self.maxTemp.setObjectName("maxTemp")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.maxTemp)
        self.chgMinLight = QtWidgets.QPushButton(Form)
        self.chgMinLight.setObjectName("chgMinLight")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chgMinLight)
        self.chgMaxLight = QtWidgets.QPushButton(Form)
        self.chgMaxLight.setObjectName("chgMaxLight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chgMaxLight)
        self.chgMinTemp = QtWidgets.QPushButton(Form)
        self.chgMinTemp.setObjectName("chgMinTemp")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chgMinTemp)
        self.chgMaxTemp = QtWidgets.QPushButton(Form)
        self.chgMaxTemp.setObjectName("chgMaxTemp")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.chgMaxTemp)
        self.horizontalLayout.addLayout(self.formLayout)

        self.retranslateUi(Form)
        self.chgMinLight.clicked.connect(self.chgMinLightVal)
        self.chgMaxLight.clicked.connect(self.chgMaxLightVal)
        self.chgMinTemp.clicked.connect(self.chgMinTempVal)
        self.chgMaxTemp.clicked.connect(self.chgMaxTempVal)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def chgMinLightVal(self):
        pass

    def chgMaxLightVal(self):
        pass

    def chgMinTempVal(self):
        pass

    def chgMaxTempVal(self):
        pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Change settings"))
        self.chgMinLight.setText(_translate("Form", "Change Min light value"))
        self.chgMaxLight.setText(_translate("Form", "Change Max light value"))
        self.chgMinTemp.setText(_translate("Form", "Change Min temp value"))
        self.chgMaxTemp.setText(_translate("Form", "Change Max temp value"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = settingsWindow()
    ui.setupSettingsWindowUi(Form)
    Form.show()
    sys.exit(app.exec_())

