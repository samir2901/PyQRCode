from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(403, 250)
        HelpWindow.setMaximumSize(QtCore.QSize(403, 250))
        icon = QtGui.QIcon.fromTheme(":/image/icon.png")
        HelpWindow.setWindowIcon(icon)
        HelpWindow.setStyleSheet("background-color: rgb(255, 161, 67);")
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headingIns = QtWidgets.QLabel(self.centralwidget)
        self.headingIns.setGeometry(QtCore.QRect(150, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.headingIns.setFont(font)
        self.headingIns.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 161, 67);")
        self.headingIns.setObjectName("headingIns")
        self.help1 = QtWidgets.QLabel(self.centralwidget)
        self.help1.setGeometry(QtCore.QRect(10, 60, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.help1.setFont(font)
        self.help1.setStyleSheet("background-color: rgb(255, 161, 67);")
        self.help1.setTextFormat(QtCore.Qt.PlainText)
        self.help1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.help1.setWordWrap(True)
        self.help1.setObjectName("help1")
        self.help2 = QtWidgets.QLabel(self.centralwidget)
        self.help2.setGeometry(QtCore.QRect(10, 140, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.help2.setFont(font)
        self.help2.setStyleSheet("background-color: rgb(255, 161, 67);")
        self.help2.setTextFormat(QtCore.Qt.PlainText)
        self.help2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.help2.setWordWrap(True)
        self.help2.setObjectName("help2")
        HelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName("menubar")
        HelpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelpWindow)
        self.statusbar.setObjectName("statusbar")
        HelpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Help"))
        self.headingIns.setText(_translate("HelpWindow", "Instructions"))
        self.help1.setText(_translate("HelpWindow", "1. Generate QRCode: Click on the Generate QRCode Button and then a new window will open there enter the data and click on Save Button. Automatically QRCode of the entered data will be generated and save at that location."))
        self.help2.setText(_translate("HelpWindow", "2. Read QRCode: Click on the Read QRCode Button and then a new window will open browse to the required image file and open it in the application. Then click on the Read QRCode Button to get the data."))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpWindow = QtWidgets.QMainWindow()
    ui = Ui_HelpWindow()
    ui.setupUi(HelpWindow)
    HelpWindow.show()
    sys.exit(app.exec_())
