# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficos.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 571)
        MainWindow.setStyleSheet("background-color: rgba(31,30, 36, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton1 = QtWidgets.QPushButton(self.centralwidget)
        self.boton1.setGeometry(QtCore.QRect(30, 20, 281, 81))
        self.boton1.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(218,224, 254, 255);\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(98, 160, 234);\n"
"}")
        self.boton1.setObjectName("boton1")
        self.boton2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton2.setGeometry(QtCore.QRect(30, 120, 281, 81))
        self.boton2.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(175,176,182, 255);\n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(154, 153, 150);\n"
"}")
        self.boton2.setObjectName("boton2")
        self.resultado = QtWidgets.QTextEdit(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(30, 230, 631, 291))
        self.resultado.setStyleSheet("background-color: rgba(52,54, 62, 255);\n"
"font: 75 17pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:22px;")
        self.resultado.setObjectName("resultado")
        self.resultado3 = QtWidgets.QLabel(self.centralwidget)
        self.resultado3.setGeometry(QtCore.QRect(330, 120, 331, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.resultado3.setFont(font)
        self.resultado3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resultado3.setStyleSheet("background-color: rgba(52,54, 62, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.resultado3.setText("")
        self.resultado3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultado3.setIndent(-1)
        self.resultado3.setObjectName("resultado3")
        self.resultado2 = QtWidgets.QLabel(self.centralwidget)
        self.resultado2.setGeometry(QtCore.QRect(330, 20, 331, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.resultado2.setFont(font)
        self.resultado2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resultado2.setStyleSheet("background-color: rgba(52,54, 62, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.resultado2.setText("")
        self.resultado2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultado2.setIndent(-1)
        self.resultado2.setObjectName("resultado2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyect-two"))
        self.boton1.setText(_translate("MainWindow", "Import file CSV"))
        self.boton2.setText(_translate("MainWindow", "Graph"))
        self.resultado.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:17pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:30pt;\"><br /></p></body></html>"))
        self.resultado3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.resultado2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
