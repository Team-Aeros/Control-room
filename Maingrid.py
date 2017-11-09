from PyQt5 import QtCore,  QtWidgets

class MainGrid():
    def __init__(self, widget, devices):
        self.devices = devices
        self.page0 = widget
        self.gridLayoutWidget = QtWidgets.QWidget(self.page0)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 540))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setGeometry(QtCore.QRect(0, 0, 800, 540))

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
            Widget = WidgetLong.name
        #for Widget in range(0, 3):   #Debug purposes
            self.dictWidgets[Widget] = self.rolluikWidget

            self.rolluikWidget[Widget] = QtWidgets.QWidget(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                               QtWidgets.QSizePolicy.Maximum)

            self.rolluikWidget[Widget].setSizePolicy(sizePolicy)
            self.rolluikWidget[Widget].setMinimumSize(QtCore.QSize(250, 100))
            self.rolluikWidget[Widget].setMaximumSize(QtCore.QSize(250, 100))
            self.rolluikWidget[Widget].setAutoFillBackground(True)
            self.rolluikWidget[Widget].setObjectName("Rolluik " + str(Widget) + "Widget")
            self.rolluik[Widget] = QtWidgets.QLabel(self.rolluikWidget[Widget])
            self.rolluik[Widget].setGeometry(QtCore.QRect(0, 0, 250, 100))
            self.rolluik[Widget].setObjectName("Rolluik" + str(Widget))
            self.rolluikWidget[Widget].setStyleSheet("border: 3px solid gray")

            self.status[Widget] = QtWidgets.QLabel(self.rolluikWidget[Widget])
            self.status[Widget].setFixedSize(100, 20)
            self.status[Widget].setAlignment(QtCore.Qt.AlignRight)
            self.status[Widget].setAutoFillBackground(True)
            self.status[Widget].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.status[Widget].setFrameShadow(QtWidgets.QFrame.Plain)
            self.status[Widget].setTextFormat(QtCore.Qt.PlainText)
            self.status[Widget].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignCenter)
            self.status[Widget].setObjectName("Status" + str(Widget))

            self.rolluik[Widget].setText(Widget)
            self.status[Widget].setText(WidgetLong.getStatus)

            self.rolluik[Widget].raise_()
            self.status[Widget].raise_()

            self.x += 1
            if (self.x%self.maxXvalue == 0):
                self.y += 1
                self.x = 0
            self.gridLayout_3.addWidget(self.rolluikWidget[Widget], self.y, self.x)

        self.ghostWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.gridLayout_3.addWidget(self.ghostWidget, 3, self.maxXvalue)

    def setStatus(self, widgetName, widgetStatus):
        self.status[widgetName].setText(widgetStatus)