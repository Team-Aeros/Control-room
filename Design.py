from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QLabel
from stringNames import stringNames
from Device import Device
from Maingrid import MainGrid
from PlotCanvas import PlotCanvas
import random
import sys
from LogWriter import LogWriter


# Main window
class Ui_MainWindow(object):
    def setupLog(self):
        self.log = LogWriter()
        self.log.resetLog()

    # sets up basic ui with buttons: manual, graphs, settings and info
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(918, 645)
        self.devices = []
        self.currentDevice = None
        self.setupLog()

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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 10, 781, 50))
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
        self.stackedWidget.setGeometry(QtCore.QRect(90, 60, 800, 540))
        # self.stackedWidget.setMinimumSize(QtCore.QSize(600, 600)) #400, 400
        # self.stackedWidget.move(100,100)
        # self.stackedWidget.setStyleSheet("background-color: black")

        # sets up maingrid and adds it to stacked widget
        self.page0 = QtWidgets.QWidget(MainWindow)
        self.mainGrid = MainGrid(self.page0, self.devices)
        self.stackedWidget.addWidget(self.mainGrid.page0)

        self.setupSettingsWindow()
        self.setupEnterDevice()
        self.setupGraphsWindow()
        self.setupManual()

        self.stackedWidget.setCurrentIndex(0)

        self.addADevice.clicked.connect(lambda: self.setIndex(2))
        self.Manual.clicked.connect(lambda: self.setIndex(4))
        self.Graphs.clicked.connect(lambda: self.setIndex(3))
        self.Settings.clicked.connect(lambda: self.setIndex(1))
        self.Info.clicked.connect(self.showInfo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def setIndex(self, index):
        self.stackedWidget.setCurrentIndex(index)

        # update devices
        # empty devicesBox
        self.devicesBox.clear()
        self.devicesBoxGraphs.clear()
        self.devicesBoxManual.clear()

        # fill devicesBox
        for device in self.devices:
            self.devicesBox.addItem(device.name)
            self.devicesBoxGraphs.addItem(device.name)
            self.devicesBoxManual.addItem(device.name)

        # set Rolluik1 and Status1
        """if len(self.devices) > 0:
            self.mainGrid.Rolluik1.setText(self.devices[0].name)
            self.mainGrid.Status1.setText(self.devices[0].getStatus())
        #print(self.stackedWidget.currentIndex())"""
        # self.minVal.setText(str(self.currentDevice.minVal))
        # print(self.stackedWidget.currentIndex())

    def setSensorType(self, type):
        """if type == "Light":
            self.temp.setDisabled(True)
            self.light.setDisabled(False)
        elif type == "Temperature":
            self.light.setDisabled(True)
            self.temp.setDisabled(False)"""

        self.sensorType = type

    """def changeMinLight(self, minLight):
        if self.checkStringForNumber(minLight):
            #minLigh = int(minLight)
            self.currentDevice.minLight = int(minLight)
            print("Light value from " + self.currentDevice.name + " changed to " + minLight)
    def changeMinTemp(self, minTemp):
        if self.checkStringForNumber(minTemp):
            #minTemp = int(minTemp)
            self.currentDevice.minTemp = int(minTemp)
            print("Temperature value from " + self.currentDevice.name + " changed to " + minTemp)"""

    def changeMinVal(self, minVal):
        if self.checkStringForNumber(minVal):
            self.currentDevice.minVal = int(minVal)
            self.log.writeInLog("i", "Minimum value from " + self.currentDevice.name + " changed to " + minVal)
        else:
            self.showPopup("e", "Not a number", "You have to enter a valid number!")
        # easter egg
        if minVal == "aeros development":
            self.showPopup("e", "Yes thats us!", "But seriously you need to enter a number")
            self.log.writeInLog("i", "EASTER EGG FOUND!!!")

    def checkStringForNumber(self, string):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        chrs = list(string)
        if len([chr for chr in chrs if chr not in numbers]) > 0: return False
        return True

    # sets up settingswidget that shows the settings
    def setupSettingsWindow(self):
        try:
            self.page1 = QtWidgets.QWidget()
            self.settingsWindowWidget = QtWidgets.QWidget(self.page1)
            self.settingsWindowWidget.setMinimumSize(QtCore.QSize(400, 160))
            self.settingsWindowWidget.setMaximumSize(QtCore.QSize(400, 160))

            layout = QtWidgets.QFormLayout(self.settingsWindowWidget)
            # self.minLight = QtWidgets.QLineEdit(self.settingsWindowWidget)
            # self.minTemp = QtWidgets.QLineEdit(self.settingsWindowWidget)
            self.minVal = QtWidgets.QLineEdit(self.settingsWindowWidget)

            """self.chgMinLight = QtWidgets.QPushButton(self.settingsWindowWidget)
            self.chgMinLight.setText("Change the min light value")
            self.chgMinLight.clicked.connect(lambda: self.changeMinLight(self.minLight.text()))

            self.chgMinTemp = QtWidgets.QPushButton(self.settingsWindowWidget)
            self.chgMinTemp.setText("Change the min temp value")
            self.chgMinTemp.clicked.connect(lambda: self.changeMinTemp(self.minTemp.text()))"""

            chgMinVal = QtWidgets.QPushButton(self.settingsWindowWidget)
            chgMinVal.setText("Change the minimum value")
            chgMinVal.clicked.connect(lambda: self.changeMinVal(self.minVal.text()))

            goBack = QtWidgets.QPushButton(self.settingsWindowWidget)
            goBack.setText("Ok")
            goBack.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

            self.devicesBox = QtWidgets.QComboBox(self.settingsWindowWidget)
            for device in self.devices:
                self.devicesBox.addItem(device.name)
            self.devicesBox.activated[str].connect(self.setCurrentDevice)

            layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minVal)
            # layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.minTemp)
            layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, chgMinVal)
            # layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chgMinTemp)
            layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, goBack)
            layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.devicesBox)

            # self.stackedWidget.insertWidget(1,self.page_1)
            self.stackedWidget.addWidget(self.page1)
            self.log.writeInLog("i", "Page 1: settings window created")
        except:
            self.log.writeInLog("w", "Could not create page 1: settings window")

    def setupGraphsWindow(self):
        try:
            self.page3 = QtWidgets.QWidget()
            self.graphWidget = QtWidgets.QWidget(self.page3)
            self.graphWidget.setGeometry(QtCore.QRect(50, 50, 400, 500))
            self.graphWidget.setMinimumSize(QtCore.QSize(600, 600))
            self.canvas = PlotCanvas(self.graphWidget)

            goBack = QtWidgets.QPushButton(self.graphWidget)
            goBack.setText("Ok")
            goBack.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
            goBack.move(450, 400)

            self.start = QtWidgets.QPushButton(self.graphWidget)
            self.start.setText("start")
            self.start.clicked.connect(self.fillGraph)
            self.start.move(450, 375)

            self.devicesBoxGraphs = QtWidgets.QComboBox(self.graphWidget)
            for device in self.devices:
                self.devicesBoxGraphs.addItem(device.name)
            self.devicesBoxGraphs.move(450, 0)
            self.devicesBoxGraphs.activated[str].connect(self.setCurrentDevice)

            self.stackedWidget.addWidget(self.page3)
            self.log.writeInLog("i", "Page 3: graphs window created")
        except:
            self.log.writeInLog("w", "Could not create page 3: graphs window")

    def fillGraph(self):
        # fill graph
        #data = [random.uniform(0.0, 100.0) for i in range(25)]  # testdata
        self.currentDevice.receive()
        data = []
        for i in range(25):
            data.append(self.currentDevice.data)
        try:
            self.canvas.plot(data, self.currentDevice.sensorType)
        except:
            self.showPopup("e", "Error: No device attached", "There is no device connected, add a device first!")

    def setupEnterDevice(self):
        try:
            self.page2 = QtWidgets.QWidget()
            self.sensorType = ""

            self.enterDeviceWidget = QtWidgets.QWidget(self.page2)
            self.enterDeviceWidget.setMinimumSize(QtCore.QSize(400, 300))
            self.enterDeviceWidget.setMaximumSize(QtCore.QSize(400, 300))

            layout = QtWidgets.QFormLayout(self.enterDeviceWidget)
            namelabel = QLabel("name")
            # lightlabel = QLabel("Min light")
            # templabel = QLabel("Min temp")
            valuelabel = QLabel("Minimum value")
            maxRollLengthLabel = QLabel("Max roll out length in meters")
            portlabel = QLabel("Port number")
            sensorlabel = QLabel("Sensor type")

            self.name = QtWidgets.QLineEdit(self.enterDeviceWidget)  # .setText("")
            # self.light = QtWidgets.QLineEdit(self.enterDeviceWidget)#.setText("0")
            # self.temp = QtWidgets.QLineEdit(self.enterDeviceWidget)#.setText("0")
            self.port = QtWidgets.QLineEdit(self.enterDeviceWidget)  # .setText("COM0")
            self.value = QtWidgets.QLineEdit(self.enterDeviceWidget)
            self.maxRollLength = QtWidgets.QLineEdit(self.enterDeviceWidget)

            self.name.setText("")
            # self.light.setText("0")
            # self.temp.setText("0")
            self.maxRollLength.setText("0")
            self.value.setText("0")
            self.port.setText("COM0")

            self.name.setMaximumSize(QtCore.QSize(100, 200))
            # self.light.setMaximumSize(QtCore.QSize(100,200))
            # self.temp.setMaximumSize(QtCore.QSize(100,200))
            self.value.setMaximumSize(QtCore.QSize(100, 200))
            self.maxRollLength.setMaximumSize(QtCore.QSize(100, 200))
            self.port.setMaximumSize(QtCore.QSize(100, 200))

            sensor = QtWidgets.QComboBox(self.enterDeviceWidget)
            sensor.addItem("Light")
            sensor.addItem("Temperature")
            sensor.setMaximumSize(QtCore.QSize(100, 200))
            sensor.activated[str].connect(self.setSensorType)

            addDevice = QtWidgets.QPushButton(self.enterDeviceWidget)
            addDevice.setText("Add Device")
            addDevice.setMaximumSize(QtCore.QSize(100, 300))
            addDevice.clicked.connect(self.addDeviceNoPar)

            goBack = QtWidgets.QPushButton(self.enterDeviceWidget)
            goBack.setText("Ok")
            goBack.setMaximumSize(QtCore.QSize(100, 200))
            goBack.clicked.connect(lambda: self.setIndex(0))

            layout.addRow(namelabel, self.name)
            # layout.addRow(lightlabel, self.light)
            # layout.addRow(templabel, self.temp)
            layout.addRow(valuelabel, self.value)
            layout.addRow(maxRollLengthLabel, self.maxRollLength)
            layout.addRow(portlabel, self.port)
            layout.addRow(sensorlabel, sensor)
            layout.addRow(addDevice, goBack)
            # self.stackedWidget.insertWidget(2,self.page_2)

            self.setSensorType("Light")
            self.stackedWidget.addWidget(self.page2)
            self.log.writeInLog("i", "Page 2: enter device window created")
        except:
            self.log.writeInLog("w", "Could not create Page 2: enter device window")

            # makes inputdialog in which you can enter a percentage

    def setupManual(self):
        try:
            self.page4 = QtWidgets.QWidget()
            self.manualWidget = QtWidgets.QWidget(self.page4)
            layout = QtWidgets.QFormLayout(self.manualWidget)

            percentageLabel = QLabel("Give percentage")
            percentage = QtWidgets.QLineEdit(self.manualWidget)
            percentage.setText("0")

            self.devicesBoxManual = QtWidgets.QComboBox(self.manualWidget)
            for device in self.devices:
                self.devicesBoxManual.addItem(device.name)
            self.devicesBoxManual.activated[str].connect(self.setCurrentDevice)

            ok = QtWidgets.QPushButton(self.manualWidget)
            ok.setText("Ok")
            ok.setMaximumSize(QtCore.QSize(100, 200))
            ok.clicked.connect(lambda: self.setIndex(0))
            ok.clicked.connect(lambda: self.rollOut(0))

            layout.addRow(percentageLabel, percentage)
            layout.addRow(self.devicesBoxManual, ok)

            self.manualWidget.setLayout(layout)
            self.stackedWidget.addWidget(self.page4)
            self.log.writeInLog("i", "Page 4: manual window created")
        except:
            self.log.writeInLog("w", "Could not create Page 4: manual window")

    def rollOut(self, int):
        self.currentDevice.rollDown()
        self.currentDevice.status = 0
        #print("Placeholder function to roll out the shutter " + str(int))

    def addDeviceNoPar(self):
        nameRes = self.name.text()
        portRes = self.port.text()
        # lightRes = int(self.light.text())
        # tempRes = int(self.temp.text())
        if self.checkStringForNumber(self.value.text()):
            valRes = int(self.value.text())
        else:
            self.showPopup("e", "Not a number", "You have to enter a valid number")
            self.value.setText("0")
            return
        try:
            maxRollRes = float(self.maxRollLength.text())
        except:
            self.showPopup("e", "Not a number", "You have to enter a valid number")
            self.value.setText("0")
            return

        self.name.setText("")
        self.port.setText("COM0")
        # self.light.setText("0")
        # self.temp.setText("0")
        self.value.setText("0")
        self.maxRollLength.setText("0")

        if nameRes == "":
            self.showPopup("e", "Error: No name", "New device can not be created without a name.")
            return

        for device in self.devices:
            if device.name == nameRes:
                self.showPopup("e", "Error: Duplicate names", "There already is a device with this name.")
                self.name.setText("")
                return
        if portRes == "COM5":
            newDevice = Device(nameRes, portRes, self.sensorType, valRes, maxRollRes)
            self.devices.append(newDevice)
            self.setCurrentDevice(self.devices[0].name)
            self.updateMaingrid(self.MainWindow)
            self.showPopup("i", "New Device", "Device with name: " + nameRes + " has been added!")
            self.log.writeInLog("i",
                                "New device added: name: " + nameRes + " | Port: " + portRes + " | Sensor type: " + self.sensorType + " | Minimum value: " + str(
                                    valRes) + " | Max roll length: " + str(maxRollRes))
        else:
            self.log.writeInLog("w", "Could not add device: " + nameRes)
            self.showPopup("e", "Could not add device!", "An error has occurred")

    def showPopup(self, type, popupText, popupIText):
        popup = QMessageBox()
        if type == "e":
            popup.setIcon(QMessageBox.Critical)
            popup.setWindowTitle("Error")
            self.log.writeInLog("w", "Error popup shown: " + popupText + " | " + popupIText)
        elif type == "i":
            popup.setIcon(QMessageBox.Information)
            popup.setWindowTitle("Info")
            self.log.writeInLog("i", "Information popup shown: " + popupText + " | " + popupIText)
        else:
            print("test")
        popup.setText(popupText)
        popup.setInformativeText(popupIText)

        popup.exec()

    def setCurrentDevice(self, name):
        for device in self.devices:
            if device.name == name:
                self.currentDevice = device
                """if self.currentDevice.sensorType == "Light":
                    self.minTemp.setDisabled(True)
                    self.minLight.setDisabled(False)
                    self.chgMinLight.setDisabled(False)
                    self.chgMinTemp.setDisabled(True)
                elif self.currentDevice.sensorType == "Temperature":
                    self.minTemp.setDisabled(False)
                    self.minLight.setDisabled(True)
                    self.chgMinLight.setDisabled(True)
                    self.chgMinTemp.setDisabled(False)"""
                # print(type(self.currentDevice))

    # sets te text
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

        # self.Rolluik1.setText(_translate("MainWindow", self.devices[0].getName()))
        # self.Status1.setText(_translate("MainWindow", "Status: " + self.devices[0].getStatus()))

    # Makes popup with info
    def showInfo(self):
        s = stringNames()
        s.setInfoText("Aeros Development", "we made this dashboard")
        string = s.getInfoText()
        title_text = string.split(";", )
        title = title_text[0]
        text = title_text[1]

        self.showPopup("i", title, text)

    def updateMaingrid(self, MainWindow):
        self.page0.setParent(None)
        self.page0 = QtWidgets.QWidget(MainWindow)
        self.mainGrid = MainGrid(self.page0, self.devices)
        self.stackedWidget.insertWidget(0, self.mainGrid.page0)  # this changed right


class main():
    def __init__(self):
        if __name__ == "__main__":
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())


mainUi = main()