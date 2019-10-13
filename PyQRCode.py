from PyQt5 import QtCore, QtGui, QtWidgets
from PyQRCodeHelp import Ui_HelpWindow
from PyQRCodeAbout import Ui_AboutWindow
from PyQRCodeGenerator import Ui_generateWindow
from PyQRCodeReader import Ui_readerWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 259)
        MainWindow.setMaximumSize(QtCore.QSize(592, 259))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon.fromTheme(":/image/icon.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(72, 72, 72);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.generateQR_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generateQR_btn.setGeometry(QtCore.QRect(90, 120, 141, 51))
        self.generateQR_btn.clicked.connect(self.generateWindowOpen)  
        font = QtGui.QFont()
        font.setFamily("Levenim MT")
        font.setPointSize(10)
        self.generateQR_btn.setFont(font)
        self.generateQR_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.generateQR_btn.setDefault(False)
        self.generateQR_btn.setFlat(False)
        self.generateQR_btn.setObjectName("generateQR_btn")

        self.readQR_btn = QtWidgets.QPushButton(self.centralwidget)
        self.readQR_btn.setGeometry(QtCore.QRect(360, 120, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Levenim MT")
        font.setPointSize(10)
        self.readQR_btn.setFont(font)
        self.readQR_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.readQR_btn.setDefault(False)
        self.readQR_btn.setFlat(False)
        self.readQR_btn.setObjectName("readQR_btn")
        self.readQR_btn.clicked.connect(self.readerWindowOpen)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(220, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 21))
        self.menubar.setObjectName("menubar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.actionAbout.setFont(font)
        self.actionAbout.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionAbout.setIconVisibleInMenu(False)
        self.actionAbout.setObjectName("actionAbout")
        self.menuView.addAction(self.actionHelp)
        self.menuView.addAction(self.actionAbout)
        self.menubar.addAction(self.menuView.menuAction())
        self.actionAbout.triggered.connect(self.aboutWindowOpen)
        self.actionHelp.triggered.connect(self.helpWindowOpen)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQRCode"))
        self.generateQR_btn.setText(_translate("MainWindow", "Generate QRCode"))
        self.readQR_btn.setText(_translate("MainWindow", "Read QRCode"))
        self.title.setText(_translate("MainWindow", "PyQRCode"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


    def helpWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.helpUI = Ui_HelpWindow()
        self.helpUI.setupUi(self.window)
        self.window.show()
        print("Help Window Opened")
        

    def aboutWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.aboutUI = Ui_AboutWindow()
        self.aboutUI.setupUi(self.window)
        self.window.show()
        print("About Window Opened")
        


    def generateWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.generatorUI = Ui_generateWindow()
        self.generatorUI.setupUi(self.window)
        self.window.show()
        print("Generator Window Opened")
        

    def readerWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.readerUI = Ui_readerWindow()
        self.readerUI.setupUi(self.window)
        self.window.show()
        print("Reader Window Opened")
        



    
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
