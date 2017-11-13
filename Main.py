from Design import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
class main():
    def __init__(self):
        if __name__ == "__main__":
            app = QtWidgets.QApplication(sys.argv)      #start main app
            self.MainWindow = QtWidgets.QMainWindow()   #define mainwindow
            ui = Ui_MainWindow()                        #define ui
            ui.setupUi(self.MainWindow)                 #setup ui
            self.MainWindow.show()                      #show mainwindow
            sys.exit(app.exec_())

mainUi = main() #exe