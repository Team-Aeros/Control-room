

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox, QGroupBox, QLabel, QLineEdit
from stringNames import *
from Device import *

#Main window
class Ui_MainWindow(object):

    #sets up basic ui with buttons: manual, graphs, settings and info
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 645)
        self.devices = []

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 81, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        self.addADevice = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addADevice.setObjectName("addADevice")
        self.verticalLayout.addWidget(self.addADevice)

        self.Manual = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Manual.setObjectName("Manual")
        self.verticalLayout.addWidget(self.Manual)

        self.Graphs = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Graphs.setObjectName("Graphs")
        self.verticalLayout.addWidget(self.Graphs)

        self.Settings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Settings.setObjectName("Settings")
        self.verticalLayout.addWidget(self.Settings)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.Info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Info.setObjectName("Info")
        self.verticalLayout.addWidget(self.Info)

        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 10, 781, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.Logo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Logo.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())

        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setMinimumSize(QtCore.QSize(0, 0))
        self.Logo.setMaximumSize(QtCore.QSize(300, 30))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Logo.setFont(font)
        self.Logo.setAutoFillBackground(True)
        self.Logo.setFrameShape(QtWidgets.QFrame.Box)
        self.Logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Logo.setObjectName("Logo")
        self.horizontalLayout_2.addWidget(self.Logo)

        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        self.fSkyTemp = QtWidgets.QFrame(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fSkyTemp.sizePolicy().hasHeightForWidth())
        self.fSkyTemp.setSizePolicy(sizePolicy)
        self.fSkyTemp.setMinimumSize(QtCore.QSize(180, 100))
        self.fSkyTemp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fSkyTemp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fSkyTemp.setObjectName("fSkyTemp")

        self.Sky = QtWidgets.QLabel(self.fSkyTemp)
        self.Sky.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.Sky.setObjectName("Sky")

        self.TempUp = QtWidgets.QLabel(self.fSkyTemp)
        self.TempUp.setGeometry(QtCore.QRect(100, 20, 75, 13))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TempUp.sizePolicy().hasHeightForWidth())

        self.TempUp.setSizePolicy(sizePolicy)
        self.TempUp.setMinimumSize(QtCore.QSize(60, 0))
        self.TempUp.setObjectName("TempUp")

        self.horizontalLayout_2.addWidget(self.fSkyTemp)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 200, 200, 200))
        self.stackedWidget.setMinimumSize(QtCore.QSize(400, 400))

        self.setupDeviceWindow()
        self.setupSettingsWindow()
        self.setupEnterDevice()
        self.stackedWidget.setCurrentIndex(0)

        self.addADevice.clicked.connect(lambda: self.setIndex(2))
        self.Manual.clicked.connect(self.toggleManual)
        self.Graphs.clicked.connect(self.showGraphs)
        self.Settings.clicked.connect(lambda: self.setIndex(1))
        self.Info.clicked.connect(self.showInfo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def setIndex(self, index):
        self.stackedWidget.setCurrentIndex(index)

        #update devices
        for i in range(0, len(self.devicesBox)):
            self.devicesBox.removeItem(i)
        for device in self.devices:
            self.devicesBox.addItem(device.getName())
        #self.devicesBox.activated[str].connect(self.setCurrentDevice)
        #print(self.stackedWidget.currentIndex())

    def setSensorType(self, type):
        self.sensorType = type

    #sets up the ui in which you can see the devices
    def setupDeviceWindow(self):
        self.page_0 = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_0)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 60, 781, 501))  # 90, 60, 781, 501
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.Rolluik1Widget = QtWidgets.QWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Rolluik1Widget.sizePolicy().hasHeightForWidth())

        self.Rolluik1Widget.setSizePolicy(sizePolicy)
        self.Rolluik1Widget.setMinimumSize(QtCore.QSize(200, 80))
        self.Rolluik1Widget.setMaximumSize(QtCore.QSize(400, 150))
        self.Rolluik1Widget.setMouseTracking(False)
        self.Rolluik1Widget.setAutoFillBackground(True)
        self.Rolluik1Widget.setObjectName("Rolluik1Widget")
        self.Rolluik1 = QtWidgets.QLabel(self.Rolluik1Widget)
        self.Rolluik1.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.Rolluik1.setObjectName("Rolluik1")

        self.Status1 = QtWidgets.QLabel(self.Rolluik1Widget)
        self.Status1.setGeometry(QtCore.QRect(150, 65, 100, 20))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status1.sizePolicy().hasHeightForWidth())

        self.Status1.setSizePolicy(sizePolicy)
        self.Status1.setAcceptDrops(False)
        self.Status1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Status1.setAutoFillBackground(True)
        self.Status1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Status1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Status1.setTextFormat(QtCore.Qt.PlainText)
        self.Status1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.Status1.setObjectName("Status1")

        self.Rolluik1.raise_()
        self.Status1.raise_()
        self.gridLayout_3.addWidget(self.Rolluik1Widget, 0, 0, 0, 0)

        #self.stackedWidget.insertWidget(0,self.page_0)
        self.stackedWidget.addWidget(self.page_0)
        #self.stackedWidget.setCurrentIndex(0)

    #sets up settingswidget that shows the settings
    def setupSettingsWindow(self):
        self.page_1 = QtWidgets.QWidget()
        self.settingsWindowWidget = QtWidgets.QWidget(self.page_1)
        self.settingsWindowWidget.setMinimumSize(QtCore.QSize(400,160))
        self.settingsWindowWidget.setMaximumSize(QtCore.QSize(400,160))

        layout = QtWidgets.QFormLayout(self.settingsWindowWidget)
        minLight = QtWidgets.QLineEdit(self.settingsWindowWidget)
        minTemp = QtWidgets.QLineEdit(self.settingsWindowWidget)

        chgMinLight = QtWidgets.QPushButton(self.settingsWindowWidget)
        chgMinLight.setText("Change the min light value")

        chgMinTemp = QtWidgets.QPushButton(self.settingsWindowWidget)
        chgMinTemp.setText("Change the min temp value")

        goBack = QtWidgets.QPushButton(self.settingsWindowWidget)
        goBack.setText("Ok")
        goBack.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.devicesBox = QtWidgets.QComboBox(self.settingsWindowWidget)
        for device in self.devices:
            self.devicesBox.addItem(device.getName())
        self.devicesBox.activated[str].connect(self.setCurrentDevice)

        layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, minLight)
        layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, minTemp)
        layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, chgMinLight)
        layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, chgMinTemp)
        layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, goBack)
        layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.devicesBox)

        #self.stackedWidget.insertWidget(1,self.page_1)
        self.stackedWidget.addWidget(self.page_1)

    def setupEnterDevice(self):
        self.page_2 = QtWidgets.QWidget()
        self.sensorType = ""
        self.enterDeviceWidget = QtWidgets.QWidget(self.page_2)
        self.enterDeviceWidget.setMinimumSize(QtCore.QSize(400, 300))
        self.enterDeviceWidget.setMaximumSize(QtCore.QSize(400, 300))

        layout = QtWidgets.QFormLayout(self.enterDeviceWidget)
        namelabel = QtWidgets.QLabel(self.enterDeviceWidget).setText("name")
        lightlabel = QtWidgets.QLabel(self.enterDeviceWidget).setText("Min light")
        templabel = QtWidgets.QLabel(self.enterDeviceWidget).setText("Min temp")
        portlabel = QtWidgets.QLabel(self.enterDeviceWidget).setText("Port number")
        sensorlabel = QtWidgets.QLabel(self.enterDeviceWidget).setText("Sensor type")

        self.name = QtWidgets.QLineEdit(self.enterDeviceWidget)#.setText("")
        self.light = QtWidgets.QLineEdit(self.enterDeviceWidget)#.setText("0")
        self.temp = QtWidgets.QLineEdit(self.enterDeviceWidget)#.setText("0")
        self.port = QtWidgets.QLineEdit(self.enterDeviceWidget)#.setText("COM0")

        self.name.setText("")
        self.light.setText("0")
        self.temp.setText("0")
        self.port.setText("COM0")

        self.name.setMaximumSize(QtCore.QSize(50,200))
        self.light.setMaximumSize(QtCore.QSize(50,200))
        self.temp.setMaximumSize(QtCore.QSize(50,200))
        self.port.setMaximumSize(QtCore.QSize(50,200))

        sensor = QtWidgets.QComboBox(self.enterDeviceWidget)
        sensor.addItem("Light")
        sensor.addItem("Temperature")
        sensor.setMaximumSize(QtCore.QSize(50,200))
        sensor.activated[str].connect(self.setSensorType)

        addDevice = QtWidgets.QPushButton(self.enterDeviceWidget)
        addDevice.setText("Add Device")
        addDevice.setMaximumSize(QtCore.QSize(100,300))
        addDevice.clicked.connect(self.addDeviceNoPar)

        goBack = QtWidgets.QPushButton(self.enterDeviceWidget)
        goBack.setText("Ok")
        goBack.setMaximumSize(QtCore.QSize(50,200))
        goBack.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        """layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, namelabel)
        layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, lightlabel)
        layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, templabel)
        layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, portlabel)
        layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, sensorlabel)
        layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, addDevice)

        layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, name)
        layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, light)
        layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, temp)
        layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, port)
        layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, sensor)
        layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, goBack)"""

        layout.addRow(namelabel, self.name)
        layout.addRow(lightlabel, self.light)
        layout.addRow(templabel, self.temp)
        layout.addRow(portlabel, self.port)
        layout.addRow(sensorlabel, sensor)
        layout.addRow(addDevice, goBack)
        #self.stackedWidget.insertWidget(2,self.page_2)
        self.stackedWidget.addWidget(self.page_2)

    def addDevice(self, name, port ,sensor,  minLight, minTemp,):
        self.devices.append(Device(name, port, sensor, minLight, minTemp))

    def addDeviceNoPar(self):
        nameRes = self.name.text()
        portRes = self.port.text()
        lightRes = int(self.light.text())
        tempRes = int(self.temp.text())
        if nameRes != "":
            new_device = Device(nameRes, portRes, self.sensorType, lightRes, tempRes)
            self.devices.append(new_device)

            device_added = QMessageBox()
            device_added.setIcon(QMessageBox.Information)
            device_added.setText("Device with name: " + nameRes + " has been added!")
            device_added.setWindowTitle("Info")
            device_added.setStandardButtons(QMessageBox.Cancel)
            device_added.exec_()
        else:
            print("must have name")

    def setCurrentDevice(self, name):
        for device in self.devices:
            if device.getName() == name:
                self.currentDevice = device

    #sets te text
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addADevice.setText(_translate("MainWindow", "Add a Device"))
        self.Manual.setText(_translate("MainWindow", "Manual"))
        self.Graphs.setText(_translate("MainWindow", "Graphs"))
        self.Settings.setText(_translate("MainWindow", "Settings"))
        self.Info.setText(_translate("MainWindow", "Info"))
        self.Logo.setText(_translate("MainWindow", "Aeros Development"))
        self.Sky.setText(_translate("MainWindow", "Sky:  Sunny"))
        self.TempUp.setText(_translate("MainWindow", "Temp: 30C"))

        #self.Rolluik1.setText(_translate("MainWindow", self.devices[0].getName()))
        #self.Status1.setText(_translate("MainWindow", "Status: " + self.devices[0].getStatus()))

    #makes inputdialog in which you can enter a percentage
    def toggleManual(self):
        print("Popup that allows to roll out shutter")
        try:
            s = stringNames()
            s.setManualText("Give percentage", "percentage: ")
            string = s.getManualText()
            title_text = string.split(";")
            title = title_text[0]
            text = title_text[1]

            res, popup = QInputDialog(MainWindow).getInt(MainWindow, title, text ,0 , 0, 100, 1) #res is input result
            popup.exec()

        except:
            pass

    #changes the central widget to graphs widget
    def showGraphs(self):
        print("Shows 2 graphs, temp and light")

    #Makes popup with info
    def showInfo(self):
        info = QMessageBox()

        s = stringNames()
        s.setInfoText("Aeros Development", "we made this dashboard")
        string = s.getInfoText()
        title_text = string.split(";",)
        title = title_text[0]
        text = title_text[1]

        info.setIcon(QMessageBox.Information)
        info.setText(title)
        info.setInformativeText(text)
        info.setWindowTitle("Info")
        info.setStandardButtons(QMessageBox.Cancel)
        info.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())