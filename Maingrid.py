from PyQt5 import QtCore,  QtWidgets

class MainGrid():
    def __init__(self, widget):
        self.page0 = widget
        self.gridLayoutWidget = QtWidgets.QWidget(self.page0)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 540))  # 90, 60, 781, 501
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        #self.gridLayoutWidget.setStyleSheet("background-color = yellow")
        self.gridLayoutWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        #self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setGeometry(QtCore.QRect(0, 0, 800, 540))
        y = 0
        x = 0

        for w in range(0, 4):
            self.Rolluik1Widget = QtWidgets.QWidget(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                               QtWidgets.QSizePolicy.Maximum)

            self.Rolluik1Widget.setSizePolicy(sizePolicy)
            self.Rolluik1Widget.setMinimumSize(QtCore.QSize(400, 150))
            self.Rolluik1Widget.setMaximumSize(QtCore.QSize(400, 150))
            self.Rolluik1Widget.setAutoFillBackground(True)
            self.Rolluik1Widget.setObjectName("Rolluik " + str(w) + "Widget")
            self.Rolluik1 = QtWidgets.QLabel(self.Rolluik1Widget)
            self.Rolluik1.setGeometry(QtCore.QRect(0, 0, 400, 300))
            self.Rolluik1.setObjectName("Rolluik" + str(w))
            self.Rolluik1Widget.setStyleSheet("background-color: red")

            self.Status1 = QtWidgets.QLabel(self.Rolluik1Widget)
            self.Status1.setFixedSize(100, 20)
            self.Status1.setAlignment(QtCore.Qt.AlignRight)
            self.Status1.setAutoFillBackground(True)
            self.Status1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Status1.setFrameShadow(QtWidgets.QFrame.Plain)
            self.Status1.setTextFormat(QtCore.Qt.PlainText)
            self.Status1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignCenter)
            self.Status1.setObjectName("Status" + str(w))
            #self.Status1.setStyleSheet("background-color = white")

            self.Rolluik1.raise_()
            self.Status1.raise_()

            if (w%2 == 0):
                y += 1
                x = 0
            self.gridLayout_3.addWidget(self.Rolluik1Widget, y, x)
            x += 1
