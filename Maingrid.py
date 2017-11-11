from PyQt5 import QtCore,  QtWidgets, QtGui

class MainGrid():
    def __init__(self, widget, devices):
        stylsheetFile = "MainGrid.css"
        fh = open(stylsheetFile)
        self.qstr = str(fh.read())


        self.devices = devices
        self.page0 = widget
        self.gridLayoutWidget = QtWidgets.QWidget(self.page0)
        self.gridLayoutWidget.setStyleSheet(self.qstr)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 910, 600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setGeometry(QtCore.QRect(0, 0, 910, 600))

        self.dictWidgets = {}
        self.rolluikWidget = {}
        self.rolluik = {}
        self.status = {}
        self.x = -1
        self.y = 0
        self.maxXvalue = 3
        #self.devices = {}

        self.createPage()

    def createPage(self):
        for WidgetLong in self.devices:
            WidgetDevice = WidgetLong.name
        #for WidgetDevice in range(0, 3):   #Debug purposes
            self.dictWidgets[WidgetDevice] = self.rolluikWidget

            self.rolluikWidget[WidgetDevice] = QtWidgets.QWidget(self.gridLayoutWidget)
            self.rolluikWidget[WidgetDevice].setAutoFillBackground(True)
            self.rolluikWidget[WidgetDevice].setStyleSheet("background-image: url(mooning.png);")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                               QtWidgets.QSizePolicy.Maximum)


            self.rolluikWidget[WidgetDevice].setSizePolicy(sizePolicy)
            self.rolluikWidget[WidgetDevice].setMinimumSize(QtCore.QSize(250, 170))
            self.rolluikWidget[WidgetDevice].setMaximumSize(QtCore.QSize(250, 170))
            self.rolluikWidget[WidgetDevice].setAutoFillBackground(True)
            self.rolluikWidget[WidgetDevice].setObjectName("Rolluik " + str(WidgetDevice) + "Widget")
            self.rolluik[WidgetDevice] = QtWidgets.QLabel(self.rolluikWidget[WidgetDevice])
            self.rolluik[WidgetDevice].setStyleSheet("font-size: 24px;"
                                                     "color: black;")
            self.rolluik[WidgetDevice].setGeometry(QtCore.QRect(10, 10, 150, 20))
            self.rolluik[WidgetDevice].setObjectName("Rolluik" + str(WidgetDevice))


            self.status[WidgetDevice] = QtWidgets.QLabel(self.rolluikWidget[WidgetDevice])
            self.status[WidgetDevice].setStyleSheet("font-size: 20px;")
            self.status[WidgetDevice].setFixedSize(100, 20)
            self.status[WidgetDevice].move(140, 140)
            self.status[WidgetDevice].setAlignment(QtCore.Qt.AlignRight)
            self.status[WidgetDevice].setAutoFillBackground(True)
            self.status[WidgetDevice].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.status[WidgetDevice].setFrameShadow(QtWidgets.QFrame.Plain)
            self.status[WidgetDevice].setTextFormat(QtCore.Qt.PlainText)
            self.status[WidgetDevice].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignCenter)
            self.status[WidgetDevice].setObjectName("Status" + str(WidgetDevice))



            self.rolluik[WidgetDevice].setText(WidgetDevice)
            self.status[WidgetDevice].setText(WidgetLong.getStatus())

            if WidgetLong.status == 1:
                self.status[WidgetDevice].setStyleSheet("color: red;")
            elif WidgetLong.status == 0:
                self.status[WidgetDevice].setStyleSheet("color: green;")
            else:
                self.status[WidgetDevice].setStyleSheet("color: black;")


            self.rolluik[WidgetDevice].raise_()
            self.status[WidgetDevice].raise_()


            self.x += 1
            if (self.x%self.maxXvalue == 0):
                self.y += 1
                self.x = 0
            self.gridLayout_3.addWidget(self.rolluikWidget[WidgetDevice], self.y, self.x)

        self.ghostFrame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.gridLayout_3.addWidget(self.ghostFrame, 3, self.maxXvalue)

    def setStatus(self, widgetName, widgetStatus):
        self.status[widgetName].setText(widgetStatus)
        if widgetStatus.status == "Rolled down":
            self.status[widgetName].setStyleSheet("color: red;")
        elif widgetStatus.status == "Rolled up":
            self.status[widgetName].setStyleSheet("color: green;")
        else:
            self.status[widgetName].setStyleSheet("color: black;")