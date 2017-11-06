from PyQt5 import QtCore,  QtWidgets

class MainGrid():
    def __init__(self, widget):
        y = 0
        x = -1
        self.dictWidgets = {}
        self.rolluikWidget = {}
        self.rolluik = {}
        self.status = {}
        self.devices = []

        self.page0 = widget
        self.gridLayoutWidget = QtWidgets.QWidget(self.page0)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 540))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setGeometry(QtCore.QRect(0, 0, 800, 540))

        for WidgetLong in self.devices:
            Widget = WidgetLong.name
            self.dictWidgets[Widget] = self.rolluikWidget

            self.rolluikWidget[Widget] = QtWidgets.QWidget(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                               QtWidgets.QSizePolicy.Maximum)

            self.rolluikWidget[Widget].setSizePolicy(sizePolicy)
            self.rolluikWidget[Widget].setMinimumSize(QtCore.QSize(400, 150))
            self.rolluikWidget[Widget].setMaximumSize(QtCore.QSize(400, 150))
            self.rolluikWidget[Widget].setAutoFillBackground(True)
            self.rolluikWidget[Widget].setObjectName("Rolluik " + str(Widget) + "Widget")
            self.rolluik[Widget] = QtWidgets.QLabel(self.rolluikWidget[Widget])
            self.rolluik[Widget].setGeometry(QtCore.QRect(0, 0, 400, 300))
            self.rolluik[Widget].setObjectName("Rolluik" + str(Widget))
            self.rolluikWidget[Widget].setStyleSheet("background-color: red")

            self.status[widget] = QtWidgets.QLabel(self.rolluikWidget[Widget])
            self.status[widget].setFixedSize(100, 20)
            self.status[widget].setAlignment(QtCore.Qt.AlignRight)
            self.status[widget].setAutoFillBackground(True)
            self.status[widget].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.status[widget].setFrameShadow(QtWidgets.QFrame.Plain)
            self.status[widget].setTextFormat(QtCore.Qt.PlainText)
            self.status[widget].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignCenter)
            self.status[widget].setObjectName("Status" + str(Widget))

            self.rolluik[Widget].raise_()
            self.status[widget].raise_()

            x += 1
            if (x%2 == 0):
                y += 1
                x = 0
            self.gridLayout_3.addWidget(self.rolluikWidget[Widget], y, x)


    def setDevices(self, devices):
        self.devices = devices

