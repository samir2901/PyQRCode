from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from pyzbar.pyzbar import decode

class Ui_readerWindow(object):
    def setupUi(self, readerWindow):
        readerWindow.setObjectName("readerWindow")
        readerWindow.resize(422, 638)
        icon = QtGui.QIcon.fromTheme(":/image/icon.png")
        readerWindow.setWindowIcon(icon)
        readerWindow.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.centralwidget = QtWidgets.QWidget(readerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.readerTitle = QtWidgets.QLabel(self.centralwidget)
        self.readerTitle.setGeometry(QtCore.QRect(120, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.readerTitle.setFont(font)
        self.readerTitle.setObjectName("readerTitle")
        self.openLabel = QtWidgets.QLabel(self.centralwidget)
        self.openLabel.setGeometry(QtCore.QRect(20, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.openLabel.setFont(font)
        self.openLabel.setObjectName("openLabel")
        self.filenameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.filenameEntry.setGeometry(QtCore.QRect(20, 100, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Raavi")
        font.setPointSize(11)
        self.filenameEntry.setFont(font)
        self.filenameEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filenameEntry.setObjectName("filenameEntry")
        self.readBtn = QtWidgets.QPushButton(self.centralwidget)
        self.readBtn.setGeometry(QtCore.QRect(260, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Levenim MT")
        font.setPointSize(10)
        self.readBtn.setFont(font)
        self.readBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.readBtn.setDefault(False)
        self.readBtn.setFlat(False)
        self.readBtn.setObjectName("readBtn")
        self.readBtn.clicked.connect(self.readQRCode)



        self.dataLabel = QtWidgets.QLabel(self.centralwidget)
        self.dataLabel.setGeometry(QtCore.QRect(20, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dataLabel.setFont(font)
        self.dataLabel.setObjectName("dataLabel")

              
        self.dataRead = QtWidgets.QTextEdit(self.centralwidget)
        self.dataRead.setGeometry(QtCore.QRect(20, 250, 381, 331))
        self.dataRead.setStyleSheet("background-color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setFamily("Raavi")
        font.setPointSize(11)
        self.dataRead.setFont(font)
        self.dataRead.setObjectName("dataRead")
        self.dataRead.setReadOnly(True)

        self.browseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.browseBtn.setGeometry(QtCore.QRect(50, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Levenim MT")
        font.setPointSize(10)
        self.browseBtn.setFont(font)
        self.browseBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browseBtn.setDefault(False)
        self.browseBtn.setFlat(False)
        self.browseBtn.setObjectName("browseBtn")
        self.browseBtn.clicked.connect(self.browseFile)


        readerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(readerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        readerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(readerWindow)
        self.statusbar.setObjectName("statusbar")
        readerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(readerWindow)
        QtCore.QMetaObject.connectSlotsByName(readerWindow)

    def retranslateUi(self, readerWindow):
        _translate = QtCore.QCoreApplication.translate
        readerWindow.setWindowTitle(_translate("readerWindow", "QRCode Reader"))
        self.readerTitle.setText(_translate("readerWindow", "PyQRCode Reader"))
        self.openLabel.setText(_translate("readerWindow", "Open File"))
        self.readBtn.setText(_translate("readerWindow", "Read QRCode"))
        self.dataLabel.setText(_translate("readerWindow", "Data From QRCode"))
        self.browseBtn.setText(_translate("readerWindow", "Browse"))

    def browseFile(self):
        global filename
        filter = "*.png"
        fm =QtWidgets.QFileDialog.getOpenFileName(None, "Open File", ".", filter)
        filename = fm[0]
        self.filenameEntry.setText(filename)
        print(filename)

    def readQRCode(self):
        try:
            image = Image.open(filename)
            decoded = decode(image)
            d = str(decoded[0].data)
            d = d[1:len(d)]
            self.dataRead.setText(d)
        except:
            msgError = QtWidgets.QMessageBox()
            msgError.setIcon(QtWidgets.QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Oops!! Error")
            msgError.exec_()                 
        
            
            
    
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    readerWindow = QtWidgets.QMainWindow()
    ui = Ui_readerWindow()
    ui.setupUi(readerWindow)
    readerWindow.show()
    sys.exit(app.exec_())
