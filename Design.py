from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel
from PyQt5.QtGui import QPixmap
from Device import Device
from Maingrid import MainGrid
from PlotCanvas import PlotCanvas
import random
from LogWriter import LogWriter
import sys
import time
from threading import Thread
import threading
from queue import Queue
from Language import Language



# Main window
class Ui_MainWindow(object):
    def setupLog(self):
        self.log = LogWriter()
        self.log.resetLog()


    #sets up basic ui with buttons: manual, graphs, settings and info
    def setupUi(self, mainWindow):

        stylesheetFile = "Stylesheet.css"       #styling
        fh = open(stylesheetFile)
        qstr = str(fh.read())

        self.MainWindow = mainWindow            #assign mainwindow
        self.MainWindow.setStyleSheet(qstr)

        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1000, 650)

        #setup basic variables
        self.devices = []
        self.currentDevice = None
        self.setupLog()
        self.mainQueue = Queue()
        self.lang = Language(0)


        #fill mainwindow
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 90, 650))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("buttonBar")

        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        self.addADevice = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addADevice.setObjectName("addADevice")
        self.addADevice.setFixedSize(90, 90)
        self.verticalLayout.addWidget(self.addADevice)

        self.Manual = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Manual.setObjectName("Manual")
        self.Manual.setFixedSize(90, 90)
        self.verticalLayout.addWidget(self.Manual)

        self.Graphs = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Graphs.setObjectName("Graphs")
        self.Graphs.setFixedSize(90, 90)
        self.verticalLayout.addWidget(self.Graphs)

        self.Settings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Settings.setObjectName("Settings")
        self.Settings.setFixedSize(90, 90)
        self.verticalLayout.addWidget(self.Settings)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.Info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Info.setObjectName("Info")
        self.Info.setFixedSize(90, 90)
        self.verticalLayout.addWidget(self.Info)

        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 0, 910, 50))
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
        self.Logo.setMaximumSize(QtCore.QSize(250, 50))

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
        pic = QPixmap('rsz_1aerosdev')
        self.Logo.setPixmap(pic)
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
        self.Sky.setGeometry(QtCore.QRect(10, 20, 75, 13))
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
        self.stackedWidget.setGeometry(QtCore.QRect(90, 50, 910, 600))
        # self.stackedWidget.setMinimumSize(QtCore.QSize(600, 600)) #400, 400
        # self.stackedWidget.move(100,100)
        # self.stackedWidget.setStyleSheet("background-color: black")

        # sets up maingrid and adds it to stacked widget
        self.page0 = QtWidgets.QWidget(self.MainWindow)
        self.mainGrid = MainGrid(self.page0, self.devices)
        self.stackedWidget.addWidget(self.mainGrid.page0)

        #sets up pages
        self.setupSettingsWindow()
        self.setupEnterDevice()
        self.setupGraphsWindow()
        self.setupManual()

        #sets starting page
        self.stackedWidget.setCurrentIndex(0)

        #binds functions to mainwindow buttons
        self.addADevice.clicked.connect(lambda: self.setIndex(2))
        self.Manual.clicked.connect(lambda: self.setIndex(4))
        self.Graphs.clicked.connect(lambda: self.setIndex(3))
        self.Settings.clicked.connect(lambda: self.setIndex(1))
        self.Info.clicked.connect(self.showInfo)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(0)

    def setIndex(self, index):
        try:
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

            #assign function to startRoll button if a device exist
            if len(self.devices) > 0:
                self.startRoll.setDisabled(False)
                if self.currentDevice.status == 1:
                    self.startRoll.clicked.connect(lambda: self.rollOut)
                    self.startRoll.setText(self.lang.but_StartRollOut)
                elif self.currentDevice.status == 0:
                    self.startRoll.clicked.connect(lambda: self.rollUp)
                    self.startRoll.setText(self.lang.but_startRollUp)
        except Exception as e:
            print(e)

    #set the selected sensortype
    def setSensorType(self, type):
        self.sensorType = type

    #change the minimum value of the current device
    def changeMinVal(self, minVal):
        try:
            if self.checkStringForNumber(minVal):
                self.currentDevice.minVal = int(minVal)
                self.log.writeInLog("i", "Minimum value from " + self.currentDevice.name + " changed to " + minVal)
            else:
                if minVal == "aeros development":
                    self.showPopup("e", self.lang.pop_TitleEasterEgg, self.lang.pop_TextEasterEgg)
                    self.log.writeInLog("i", "EASTER EGG FOUND!!!")
                self.showPopup("e", self.lang.pop_TitleNotValidNumber, self.lang.pop_TextNotValidNumber)
        except:
            self.showPopup("e", self.lang.pop_TitleDevNotAttached, self.lang.pop_TextDevNotAttached)


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
            self.minVal.setText("0")

            self.chgMinVal = QtWidgets.QPushButton(self.settingsWindowWidget)
            self.chgMinVal.setText(self.lang.but_ChgMinVal)
            self.chgMinVal.clicked.connect(lambda: self.changeMinVal(self.minVal.text()))

            self.goBack = QtWidgets.QPushButton(self.settingsWindowWidget)
            self.goBack.setText(self.lang.but_Ok)
            self.goBack.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

            self.devicesBox = QtWidgets.QComboBox(self.settingsWindowWidget)
            for device in self.devices:
                self.devicesBox.addItem(device.name)
            self.devicesBox.activated[str].connect(self.setCurrentDevice)

            self.languageBox = QtWidgets.QComboBox(self.settingsWindowWidget)
            self.languageBox.addItem("English")
            self.languageBox.addItem("Nederlands")
                #could add more languages
            self.languageBox.activated[str].connect(self.changeLanguage)

            layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minVal)
            # layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.minTemp)
            layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chgMinVal)
            # layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chgMinTemp)
            layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.goBack)
            layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.devicesBox)
            layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.languageBox)

            # self.stackedWidget.insertWidget(1,self.page_1)
            self.stackedWidget.addWidget(self.page1)
            self.log.writeInLog("i", "Page 1: settings window created")
        except Exception as e:
            print(e)
            self.log.writeInLog("w", "Could not create page 1: settings window")

    #change the language,
    def changeLanguage(self, lang):
        if lang == "English":
            self.retranslateUi(0)
        elif lang == "Nederlands":
            self.retranslateUi(1)

    #setup page3 containing the graph
    def setupGraphsWindow(self):
        try:
            self.page3 = QtWidgets.QWidget()
            self.graphWidget = QtWidgets.QWidget(self.page3)
            self.graphWidget.setGeometry(QtCore.QRect(50, 50, 400, 500))
            self.graphWidget.setMinimumSize(QtCore.QSize(600, 600))
            self.canvas = PlotCanvas(self.graphWidget)

            self.goBack2 = QtWidgets.QPushButton(self.graphWidget)
            self.goBack2.setText(self.lang.but_Ok)
            self.goBack2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
            self.goBack2.move(450, 400)

            self.update = QtWidgets.QPushButton(self.graphWidget)
            self.update.setText(self.lang.but_Update)
            self.update.clicked.connect(self.fillGraph)
            self.update.move(450, 375)

            self.devicesBoxGraphs = QtWidgets.QComboBox(self.graphWidget)
            for device in self.devices:
                self.devicesBoxGraphs.addItem(device.name)
            self.devicesBoxGraphs.move(450, 0)
            self.devicesBoxGraphs.activated[str].connect(self.setCurrentDevice)

            self.stackedWidget.addWidget(self.page3)
            self.log.writeInLog("i", "Page 3: graphs window created")
        except:
            self.log.writeInLog("w", "Could not create page 3: graphs window")
    #fill graph
    def fillGraph(self):
        dataList = []
        try:
            q = self.currentDevice.getQueue()
        except:# Exception as e:
            #print(e)
            self.showPopup("e", self.lang.pop_TitleDevNotAttached, self.lang.pop_TextDevNotAttached)
            return
        # fill graph
        #print("test1")
        #print("test2")
        #print(self.currentDevice.queue.get())
        transmis = None
        try:
            for i in range(10):
               #transmis = q.get(True, 2)
                if transmis == None:
                    if self.currentDevice.sensorType == "Light":
                        dataList.append(random.uniform(50,100))
                    elif self.currentDevice.sensorType == "Temperature":
                        dataList.append(random.uniform(20,25))
                else:
                    self.log.writeInLog("i", "Data from " + self.currentDevice.name + " received: " + str(transmis))
                    dataList.append(transmis)
                #time.sleep(1)
        except:
            pass
        try:
            #print("test6")
            self.canvas.plot(dataList, self.currentDevice.sensorType)
            #time.sleep(1)
        except Exception as e:
            print(e)

    #setup page2 containing the settingswindow
    def setupEnterDevice(self):
        try:
            self.page2 = QtWidgets.QWidget()
            self.sensorType = ""

            self.enterDeviceWidget = QtWidgets.QWidget(self.page2)
            self.enterDeviceWidget.setMinimumSize(QtCore.QSize(400, 300))
            self.enterDeviceWidget.setMaximumSize(QtCore.QSize(400, 300))

            layout = QtWidgets.QFormLayout(self.enterDeviceWidget)
            namelabel = QLabel(self.lang.lab_Name)
            # lightlabel = QLabel("Min light")
            # templabel = QLabel("Min temp")
            valuelabel = QLabel(self.lang.lab_MinVal)
            maxRollLengthLabel = QLabel(self.lang.lab_MaxRollLength)
            portlabel = QLabel(self.lang.lab_PortNum)
            sensorlabel = QLabel(self.lang.lab_SensorType)

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

            self.sensor = QtWidgets.QComboBox(self.enterDeviceWidget)
            self.sensor.addItem(self.lang.selBox_light)
            self.sensor.addItem(self.lang.selBox_temp)
            self.sensor.setMaximumSize(QtCore.QSize(100, 200))
            self.sensor.activated[str].connect(self.setSensorType)

            self.addDevice = QtWidgets.QPushButton(self.enterDeviceWidget)
            self.addDevice.setText(self.lang.but_AddDevice)
            self.addDevice.setMaximumSize(QtCore.QSize(120, 300))
            self.addDevice.clicked.connect(self.addDeviceNoPar)

            self.goBack3 = QtWidgets.QPushButton(self.enterDeviceWidget)
            self.goBack3.setText(self.lang.but_Ok)
            self.goBack3.setMaximumSize(QtCore.QSize(100, 200))
            self.goBack3.clicked.connect(lambda: self.setIndex(0))

            layout.addRow(namelabel, self.name)
            # layout.addRow(lightlabel, self.light)
            # layout.addRow(templabel, self.temp)
            layout.addRow(valuelabel, self.value)
            layout.addRow(maxRollLengthLabel, self.maxRollLength)
            layout.addRow(portlabel, self.port)
            layout.addRow(sensorlabel, self.sensor)
            layout.addRow(self.addDevice, self.goBack3)
            # self.stackedWidget.insertWidget(2,self.page_2)

            self.setSensorType("Light")
            self.stackedWidget.addWidget(self.page2)
            self.log.writeInLog("i", "Page 2: enter device window created")
        except:
            self.log.writeInLog("w", "Could not create Page 2: enter device window")

            # makes inputdialog in which you can enter a percentage
    #setup page4 containing the manual mode window
    def setupManual(self):
        try:
            self.page4 = QtWidgets.QWidget()
            self.manualWidget = QtWidgets.QWidget(self.page4)
            layout = QtWidgets.QFormLayout(self.manualWidget)

            self.startRoll = QtWidgets.QPushButton(self.manualWidget)
            self.startRoll.setText(self.lang.but_StartRoll)
            self.startRoll.setDisabled(True)


            self.devicesBoxManual = QtWidgets.QComboBox(self.manualWidget)
            for device in self.devices:
                self.devicesBoxManual.addItem(device.name)
            self.devicesBoxManual.activated[str].connect(self.setCurrentDevice)

            self.ok = QtWidgets.QPushButton(self.manualWidget)
            self.ok.setText(self.lang.but_Ok)
            self.ok.setMaximumSize(QtCore.QSize(100, 200))
            self.ok.clicked.connect(lambda: self.setIndex(0))

            layout.addRow(self.devicesBoxManual, self.startRoll)
            layout.addRow(self.ok, self.ok)

            self.manualWidget.setLayout(layout)
            self.stackedWidget.addWidget(self.page4)
            self.log.writeInLog("i", "Page 4: manual window created")
        except Exception as e:
            print(e)
            self.log.writeInLog("w", "Could not create Page 4: manual window")

    #roll out the selected device
    def rollOut(self):
        self.showPopup("i", self.lang.pop_TitleRollOut, self.currentDevice.name + self.lang.pop_TextRollOut)
        self.log.writeInLog("i", self.currentDevice.name + " rolled out")
        self.currentDevice.rollDown()
        self.currentDevice.status = 0
        self.updateMaingrid(self.MainWindow)

    #roll up the selected device
    def rollUp(self):
        self.showPopup("i", self.lang.pop_TitleRollUp, self.currentDevice.name + self.lang.pop_TextRollUp)
        self.log.writeInLog("i", self.currentDevice.name + " rolled up")
        self.currentDevice.rollUp()
        self.currentDevice.status = 1
        self.updateMaingrid(self.MainWindow)

    #connect to the device and add it to the dashboard
    def addDeviceNoPar(self):
        if not self.checkStringForNumber(self.name.text()):
            nameRes = self.name.text()
        else:
            self.showPopup("e", self.lang.pop_TitleNotValidName, self.lang.pop_TextNotValidName)
            self.name.setText("")
            return

        if "COM" in self.port.text():
            portRes = self.port.text()
        else:
            self.showPopup("e", self.lang.pop_TitleNotValidPort, self.lang.pop_TextNotValidPort)
            self.port.setText("COM0")
            return

        if self.checkStringForNumber(self.value.text()):
            valRes = int(self.value.text())
        else:
            self.showPopup("e", self.lang.pop_TitleNotValidNumber, self.lang.pop_TextNotValidNumber)
            self.value.setText("0")
            return

        try:
            maxRollRes = float(self.maxRollLength.text())
        except:
            self.showPopup("e", self.lang.pop_TitleNotValidNumber, self.lang.pop_TextNotValidNumber)
            self.maxRollLength.setText("0")
            return

        self.name.setText("")
        self.port.setText("COM0")
        self.value.setText("0")
        self.maxRollLength.setText("0")

        if nameRes == "":
            self.showPopup("e", self.lang.pop_TitleNoName, self.lang.pop_TextNoName)
            return

        for device in self.devices:
            if device.name == nameRes:
                self.showPopup("e", self.lang.pop_TitleDupNames, self.lang.pop_TextDupNames)
                self.name.setText("")
                return
        try:
            newDevice = Device(nameRes, portRes, self.sensorType, valRes, maxRollRes, self.mainQueue)  # lightRes, tempRes)
            self.devices.append(newDevice)
            self.setCurrentDevice(self.devices[0].name)
            try:
                receiving = Thread(target=self.currentDevice.receive)
                receiving.daemon = True
                receiving.start()
            except Exception as e:
                print(e)
            self.log.writeInLog("i",
                                "New device added: name: " + nameRes + " | Port: " + portRes + " | Sensor type: " + self.sensorType + " | Minimum value: " + str(
                                    valRes) + " | Max roll length: " + str(maxRollRes))
            self.showPopup("i", self.lang.pop_TitleNewDevice, self.lang.pop_TextNewDevice_1  + nameRes + self.lang.pop_TextNewDevice_2)
            try:
                self.updateMaingrid(self.MainWindow)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
            self.log.writeInLog("w", "Could not add device: " + nameRes)
            self.showPopup("e", self.lang.pop_TitleNoNewDevice, self.lang.pop_TextNoNewDevice)
            newDevice = None

    #show a popup, can be error or info
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

        popup.setText(popupText)
        popup.setInformativeText(popupIText)

        popup.exec()

    #set the current selected device
    def setCurrentDevice(self, name):
        for device in self.devices:
            if device.name == name:
                self.currentDevice = device

    # sets te text in the given language
    def retranslateUi(self, type):
        # choose language
        self.lang.setLang(type)
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addADevice.setText(_translate("MainWindow", self.lang.but_AddADevice))
        self.Manual.setText(_translate("MainWindow", self.lang.but_Manual))
        self.Graphs.setText(_translate("MainWindow", self.lang.but_Graphs))
        self.Settings.setText(_translate("MainWindow", self.lang.but_Settings))
        self.Info.setText(_translate("MainWindow", self.lang.but_Info))
        self.Sky.setText(_translate("MainWindow", self.lang.lab_Sky))
        self.TempUp.setText(_translate("MainWindow", self.lang.lab_Temp))
        self.startRoll.setText("Roll out")
        self.startRoll.setText("Roll up")
        self.goBack.setText(self.lang.but_Ok)
        self.chgMinVal.setText(self.lang.but_ChgMinVal)
        self.goBack2.setText(self.lang.but_Ok)
        self.update.setText(self.lang.but_Update)
        self.addDevice.setText(self.lang.but_AddDevice)
        self.sensor.clear()
        self.sensor.addItem(self.lang.selBox_light)
        self.sensor.addItem(self.lang.selBox_temp)
        self.goBack3.setText(self.lang.but_Ok)
        self.startRoll.setText(self.lang.but_StartRoll)
        self.ok.setText(self.lang.but_Ok)

    # Makes popup with info
    def showInfo(self):
        self.showPopup("i", self.lang.pop_TitleInfo, self.lang.pop_TextInfo)

    #update the maingrid
    def updateMaingrid(self, MainWindow):
        self.page0.setParent(None)
        self.page0 = QtWidgets.QWidget(MainWindow)
        self.mainGrid = MainGrid(self.page0, self.devices)
        self.stackedWidget.insertWidget(0, self.mainGrid.page0)  # this changed right
