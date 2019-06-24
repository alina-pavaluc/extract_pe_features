from PyQt5 import QtCore, QtWidgets

# from run_app_gui import Ui_MainWindow


class Ui_TrainWindow(object):

    def __init__(self, window):
        self.TrainWindow = window
        self.setup(self.TrainWindow)
    def setup(self, TrainWindow):
        TrainWindow.setObjectName("TrainWindow")
        TrainWindow.resize(769, 459)
        TrainWindow.setStyleSheet(
            "QWidget {background-color:#202020; color: white; font: 75 10pt \"Palatino Linotype\"; }\n"
            "")
        self.centralwidget = QtWidgets.QWidget(TrainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.selectCleanButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectCleanButton.setGeometry(QtCore.QRect(120, 150, 181, 41))
        self.selectCleanButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color: white}\n"
            "")
        self.selectCleanButton.setObjectName("selectCleanButton")
        self.selctMalwareData = QtWidgets.QPushButton(self.centralwidget)
        self.selctMalwareData.setGeometry(QtCore.QRect(120, 220, 181, 41))
        self.selctMalwareData.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color: white}")
        self.selctMalwareData.setObjectName("selctMalwareData")
        self.trainModelButton = QtWidgets.QPushButton(self.centralwidget)
        self.trainModelButton.setGeometry(QtCore.QRect(410, 250, 231, 81))
        self.trainModelButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: rgb(172, 16, 186); color:white}\n"
            "")
        self.trainModelButton.setObjectName("trainModelButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 511, 41))
        self.label.setObjectName("label")
        self.selectParameters = QtWidgets.QPushButton(self.centralwidget)
        self.selectParameters.setGeometry(QtCore.QRect(120, 290, 181, 41))
        self.selectParameters.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color: white}")
        self.selectParameters.setObjectName("selectParameters")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(10, 390, 141, 41))
        self.backButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: rgb(171, 171, 171); color: white}")
        self.backButton.setObjectName("backButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(500, 150, 141, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 160, 151, 20))
        self.label_2.setObjectName("label_2")
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setGeometry(QtCore.QRect(690, 0, 81, 41))
        self.helpButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: rgb(171, 171, 171); color: white}")
        self.helpButton.setObjectName("helpButton")
        TrainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TrainWindow)
        self.statusbar.setObjectName("statusbar")
        TrainWindow.setStatusBar(self.statusbar)

        self.backButton.clicked.connect(self.goToMainWindow)

        self.retranslate(TrainWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainWindow)
        self.selectParameters.clicked.connect(self.setFile)
        self.selctMalwareData.clicked.connect(self.setDirectory)
        self.selectCleanButton.clicked.connect(self.setDirectory)



    def goToMainWindow(self):
        self.window = QtWidgets.QMainWindow()
        from run_app_gui import Ui_MainWindow
        self.ui = Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)

        self.window.show()
        self.TrainWindow.hide()

    def setDirectory(self):

        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Select directory", "")
        print(directory)


    def setFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select file", "", "Text Files (*.txt)")
        print(fileName)
    def retranslate(self, TrainWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainWindow.setWindowTitle(_translate("TrainWindow", "Malware detector"))
        self.selectCleanButton.setText(_translate("TrainWindow", "Select clean data"))
        self.selctMalwareData.setText(_translate("TrainWindow", "Select malware data"))
        self.trainModelButton.setText(_translate("TrainWindow", "TRAIN"))
        self.label.setText(_translate("TrainWindow", "Here you can train you own Random Forest Classification Model"))
        self.selectParameters.setText(_translate("TrainWindow", "Select file with parameters"))
        self.backButton.setText(_translate("TrainWindow", "Back"))
        self.label_2.setText(_translate("TrainWindow", "Enter model name: "))
        self.helpButton.setText(_translate("TrainWindow", "Help"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TrainWindow = QtWidgets.QMainWindow()
    ui = Ui_TrainWindow()
    ui.setup(TrainWindow)
    TrainWindow.show()
    sys.exit(app.exec_())
