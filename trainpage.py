# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alina\Desktop\loadpage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 459)
        MainWindow.setStyleSheet("QWidget {background-color:#202020; color: white; font: 75 10pt \"Palatino Linotype\"; }\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.selectCleanButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectCleanButton.setGeometry(QtCore.QRect(120, 150, 181, 41))
        self.selectCleanButton.setStyleSheet("QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color: white}\n"
"")
        self.selectCleanButton.setObjectName("selectCleanButton")
        self.selctMalwareData = QtWidgets.QPushButton(self.centralwidget)
        self.selctMalwareData.setGeometry(QtCore.QRect(120, 220, 181, 41))
        self.selctMalwareData.setStyleSheet("QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color: white}")
        self.selctMalwareData.setObjectName("selctMalwareData")
        self.trainModelButton = QtWidgets.QPushButton(self.centralwidget)
        self.trainModelButton.setGeometry(QtCore.QRect(410, 250, 231, 81))
        self.trainModelButton.setStyleSheet("QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: rgb(172, 16, 186); color:white}\n"
"")
        self.trainModelButton.setObjectName("trainModelButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 511, 41))
        self.label.setObjectName("label")
        self.selctMalwareData_2 = QtWidgets.QPushButton(self.centralwidget)
        self.selctMalwareData_2.setGeometry(QtCore.QRect(120, 290, 181, 41))
        self.selctMalwareData_2.setStyleSheet("QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: #2195f3; color: white}")
        self.selctMalwareData_2.setObjectName("selctMalwareData_2")
        self.selctMalwareData_3 = QtWidgets.QPushButton(self.centralwidget)
        self.selctMalwareData_3.setGeometry(QtCore.QRect(10, 390, 141, 41))
        self.selctMalwareData_3.setStyleSheet("QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: rgb(171, 171, 171); color: white}")
        self.selctMalwareData_3.setObjectName("selctMalwareData_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(500, 150, 141, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 160, 151, 20))
        self.label_2.setObjectName("label_2")
        self.selctMalwareData_4 = QtWidgets.QPushButton(self.centralwidget)
        self.selctMalwareData_4.setGeometry(QtCore.QRect(690, 0, 81, 41))
        self.selctMalwareData_4.setStyleSheet("QPushButton {font: 75 9pt \"MS Shell Dlg 2\"; background-color: rgb(171, 171, 171); color: white}")
        self.selctMalwareData_4.setObjectName("selctMalwareData_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Malware detector"))
        self.selectCleanButton.setText(_translate("MainWindow", "Select clean data"))
        self.selctMalwareData.setText(_translate("MainWindow", "Select malware data"))
        self.trainModelButton.setText(_translate("MainWindow", "TRAIN"))
        self.label.setText(_translate("MainWindow", "Here you can train you own Random Forest Classification Model"))
        self.selctMalwareData_2.setText(_translate("MainWindow", "Select file with parameters"))
        self.selctMalwareData_3.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "Enter model name: "))
        self.selctMalwareData_4.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

