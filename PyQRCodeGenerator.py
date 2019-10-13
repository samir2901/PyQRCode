from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode


class Ui_generateWindow(object):
    def setupUi(self, generateWindow):
        generateWindow.setObjectName("generateWindow")
        generateWindow.resize(407, 653)
        generateWindow.setMaximumSize(QtCore.QSize(407, 653))
        icon = QtGui.QIcon.fromTheme(":/image/icon.png")
        generateWindow.setWindowIcon(icon)
        generateWindow.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.centralwidget = QtWidgets.QWidget(generateWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.generatorTitle = QtWidgets.QLabel(self.centralwidget)
        self.generatorTitle.setGeometry(QtCore.QRect(100, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.generatorTitle.setFont(font)
        self.generatorTitle.setObjectName("generatorTitle")
        self.dataLabel = QtWidgets.QLabel(self.centralwidget)
        self.dataLabel.setGeometry(QtCore.QRect(20, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(11)
        self.dataLabel.setFont(font)
        self.dataLabel.setObjectName("dataLabel")



        self.dataEntry = QtWidgets.QTextEdit(self.centralwidget)
        self.dataEntry.setGeometry(QtCore.QRect(20, 100, 371, 311))
        font = QtGui.QFont()
        font.setFamily("Raavi")
        font.setPointSize(11)
        self.dataEntry.setFont(font)
        self.dataEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dataEntry.setObjectName("dataEntry")
        self.saveLabel = QtWidgets.QLabel(self.centralwidget)
        self.saveLabel.setGeometry(QtCore.QRect(20, 430, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.saveLabel.setFont(font)
        self.saveLabel.setObjectName("saveLabel")



        self.filenameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.filenameEntry.setGeometry(QtCore.QRect(20, 470, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Raavi")
        font.setPointSize(11)
        self.filenameEntry.setFont(font)
        self.filenameEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filenameEntry.setObjectName("filenameEntry")
        self.filenameEntry.setReadOnly(True)
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(260, 540, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Levenim MT")
        font.setPointSize(10)
        self.saveBtn.setFont(font)
        self.saveBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.saveBtn.setDefault(False)
        self.saveBtn.setFlat(False)
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.clicked.connect(self.makeQRCode)


        self.browseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.browseBtn.setGeometry(QtCore.QRect(60, 540, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Levenim MT")
        font.setPointSize(10)
        self.browseBtn.setFont(font)
        self.browseBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browseBtn.setDefault(False)
        self.browseBtn.setFlat(False)
        self.browseBtn.setObjectName("browseBtn")
        self.browseBtn.clicked.connect(self.browseFile)


        generateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(generateWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 21))
        self.menubar.setObjectName("menubar")
        generateWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(generateWindow)
        self.statusbar.setObjectName("statusbar")
        generateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(generateWindow)
        QtCore.QMetaObject.connectSlotsByName(generateWindow)

    def retranslateUi(self, generateWindow):
        _translate = QtCore.QCoreApplication.translate
        generateWindow.setWindowTitle(_translate("generateWindow", "QRCode Generator"))
        self.generatorTitle.setText(_translate("generateWindow", "PyQRCode Generator"))
        self.dataLabel.setText(_translate("generateWindow", "Enter the data here"))
        self.saveLabel.setText(_translate("generateWindow", "Save File As"))
        self.saveBtn.setText(_translate("generateWindow", "Save"))
        self.browseBtn.setText(_translate("generateWindow", "Browse"))

    def browseFile(self):
        global filename
        fm = QtWidgets.QFileDialog.getSaveFileName(None,"Save File As",".","*.png")
        filename = fm[0]
        self.filenameEntry.setText(filename)
        print(filename)
    
    def makeQRCode(self):
        try:
            txt = self.dataEntry.toPlainText()
            qr = qrcode.QRCode(version=1,box_size=10,border=5)
            qr.add_data(txt)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            print("File Converted")            
            msgDone = QtWidgets.QMessageBox()
            msgDone.setIcon(QtWidgets.QMessageBox.Information)
            msgDone.setWindowTitle("Done")
            msgDone.setText("QRCode is Generated.")
            msgDone.exec_()
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
    generateWindow = QtWidgets.QMainWindow()
    ui = Ui_generateWindow()
    ui.setupUi(generateWindow)
    generateWindow.show()
    sys.exit(app.exec_())
