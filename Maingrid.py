from PyQt5 import QtCore,  QtWidgets

class MainGrid():
    def __init__(self, widget):
        self.page0 = widget
        self.gridLayoutWidget = QtWidgets.QWidget(self.page0)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 60, 781, 501))  # 90, 60, 781, 501
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.rolluik1Widget = QtWidgets.QWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rolluik1Widget.sizePolicy().hasHeightForWidth())

        self.rolluik1Widget.setSizePolicy(sizePolicy)
        self.rolluik1Widget.setMinimumSize(QtCore.QSize(200, 80))
        self.rolluik1Widget.setMaximumSize(QtCore.QSize(400, 150))
        self.rolluik1Widget.setMouseTracking(False)
        self.rolluik1Widget.setAutoFillBackground(True)
        self.rolluik1Widget.setObjectName("Rolluik1Widget")
        self.Rolluik1 = QtWidgets.QLabel(self.rolluik1Widget)
        self.Rolluik1.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.Rolluik1.setObjectName("Rolluik1")

        self.Status1 = QtWidgets.QLabel(self.rolluik1Widget)
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
        self.gridLayout_3.addWidget(self.rolluik1Widget, 0, 0, 0, 0)

