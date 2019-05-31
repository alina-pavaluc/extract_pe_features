from PyQt5 import QtWidgets, QtCore

from classifier import Classifier


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 449)
        MainWindow.setStyleSheet(
            "QWidget {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 81, 0, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.selectFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectFileButton.setGeometry(QtCore.QRect(20, 320, 121, 41))
        self.selectFileButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: rgb(0, 62, 0); color: white}\n"
            "")
        self.selectFileButton.setObjectName("selectFileButton")
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(20, 380, 121, 41))
        self.scanButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: rgb(0, 62, 0); color: white}")
        self.scanButton.setObjectName("scanButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 20, 581, 401))
        self.listWidget.setStyleSheet("QListWidget {background-color: rgb(235, 245, 242)}")
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selectFileButton.clicked.connect(self.setFile)
        self.scanButton.clicked.connect(self.setDirectory)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Virus Scanner"))
        self.selectFileButton.setText(_translate("MainWindow", "Select a file"))
        self.scanButton.setText(_translate("MainWindow", "Scan a directory"))

    def setFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select file", "")
        if fileName:
            self.print_classification(fileName)

    def print_classification(self, filename):
        label = classifier.classify_file(filename)
        self.listWidget.addItem(filename + " - " + label[0] + " probability: " + str(label[1]))

    def setDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Select directory", "")
        if directory:
            self.print_classification_folder(directory)

    def print_folder(self, dir):
        self.listWidget.addItem(dir)

    def print_classification_folder(self, directory):
        classified_files = classifier.scan_folder(directory)
        for item in classified_files:
            self.listWidget.addItem(item[0] + " - " + item[1][0] + " probability: " + str(item[1][1]))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    classifier = Classifier('C:\\Users\\Alina\\PycharmProjects\\licenta2\\finalized_model_random_forest.sav')

    MainWindow.show()
    sys.exit(app.exec_())
