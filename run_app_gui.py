import PyQt5
from PyQt5 import QtCore, QtWidgets

from classifier import Classifier
from trainpage import *


class Ui_MainWindow(object):

    def __init__(self, window):
        self.MainWindow = window
        self.setupUi(self.MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 449)
        MainWindow.setStyleSheet("QWidget {background-color:#202020}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.selectFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectFileButton.setGeometry(QtCore.QRect(20, 20, 121, 41))
        self.selectFileButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color: white}\n"
            "")
        self.selectFileButton.setObjectName("selectFileButton")
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(20, 80, 121, 41))
        self.scanButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color: white}")
        self.scanButton.setObjectName("scanButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 20, 581, 401))
        self.listWidget.setStyleSheet("QListWidget {background-color:#404040; color:white}")
        self.listWidget.setObjectName("listWidget")
        self.UseDefaultButton = QtWidgets.QPushButton(self.centralwidget)
        self.UseDefaultButton.setGeometry(QtCore.QRect(20, 260, 121, 41))
        self.UseDefaultButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color:white}\n"
            "")
        self.UseDefaultButton.setObjectName("UseDefaultButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 140, 121, 91))
        self.label.setStyleSheet("QLabel{color:red; font: 75 9pt \"MS Shell Dlg 2\"}")
        self.label.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.label.setText("")
        self.label.setObjectName("label")

        self.loadModelButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadModelButton.setGeometry(QtCore.QRect(20, 380, 121, 41))
        self.loadModelButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color:white}\n"
            "")
        self.loadModelButton.setObjectName("loadModelButton")
        self.trainModelButton = QtWidgets.QPushButton(self.centralwidget)
        self.trainModelButton.setGeometry(QtCore.QRect(20, 320, 121, 41))
        self.trainModelButton.setStyleSheet(
            "QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color:white}\n"
            "")
        self.trainModelButton.setObjectName("trainModelButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selectFileButton.clicked.connect(self.setFile)
        self.scanButton.clicked.connect(self.setDirectory)
        self.trainModelButton.clicked.connect(self.goToTrainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Malware Detector"))
        self.selectFileButton.setText(_translate("MainWindow", "Select a file"))
        self.scanButton.setText(_translate("MainWindow", "Scan a directory"))
        self.loadModelButton.setText(_translate("MainWindow", "Load model"))
        self.trainModelButton.setText(_translate("MainWindow", "Train new model"))
        self.UseDefaultButton.setText(_translate("MainWindow", "Use default model"))

    def setFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select file", ".")
        if fileName:
            self.print_classification(fileName)

    def goToTrainWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TrainWindow(self.window)
        self.ui.setup(self.window)
        self.window.show()
        self.MainWindow.hide()

    def print_classification(self, filename):
        classifier = Classifier('C:\\Users\\Alina\\PycharmProjects\\licenta2\\finalized_model_random_forest.sav')
        label = classifier.classify_file(filename)
        self.listWidget.addItem(filename + " - " + label[0] + " probability: " + str(label[1]))

    def setDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Select directory", "")
        if directory:
            self.print_classification_folder(directory)

    def print_folder(self, dir):
        self.listWidget.addItem(dir)

    def print_classification_folder(self, directory):
        classifier = Classifier('C:\\Users\\Alina\\PycharmProjects\\licenta2\\finalized_model_random_forest.sav')

        classified_files = list(classifier.scan_folder(directory))
        malware_count = sum(1 for i in classified_files if i[1][0] == 'malware')
        file_count = len(classified_files)

        self.label.setText(str(malware_count) + "/" + str(file_count) + " malware")

        self.listWidget.clear()
        for item in classified_files:
            self.listWidget.addItem(item[0] + " - " + item[1][0] + " probability: " + str(item[1][1]))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    # classifier = Classifier('C:\\Users\\Alina\\PycharmProjects\\licenta2\\finalized_model_random_forest.sav')
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
