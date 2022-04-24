# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_pageTyUaXt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Loginwindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 400)
        MainWindow.setStyleSheet(u"background-color: rgb(27, 26, 23);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(27, 26, 23);\n"
"	color:rgb(220,220,220);\n"
"}")
        self.DropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.DropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, -10, 141, 101))
        font = QFont()
        font.setFamily(u"Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"background-image: url(E:\CV\Abhidrishya\Abhidrishya_logo.png);")
        self.label.setPixmap(QPixmap(u"E:\CV\Abhidrishya\Abhidrishya_logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.DropShadowFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 100, 591, 41))
        self.label_2.setStyleSheet(u"\n"
"font: 75 19pt \"Gill Sans MT\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.DropShadowFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 170, 141, 41))
        self.label_3.setStyleSheet(u"\n"
"font: 75 14pt \"Gill Sans MT\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.DropShadowFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 210, 141, 41))
        self.label_4.setStyleSheet(u"\n"
"font: 75 14pt \"Gill Sans MT\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.DropShadowFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 180, 131, 20))
        self.lineEdit_2 = QLineEdit(self.DropShadowFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(300, 220, 131, 21))
        self.pushButton = QPushButton(self.DropShadowFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 280, 141, 41))
        self.pushButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.057, y1:1, x2:1, y2:0.926, stop:0 rgba(240, 165, 0, 255), stop:1 rgba(238, 240, 113, 255));\n"
"font: 75 14pt \"Gill Sans MT\";\n"
"color: rgb(27, 26, 23);\n"
"border: 3px solid rgb(27, 26, 23);\n"
"border-radius: 8px;")

        self.verticalLayout.addWidget(self.DropShadowFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

