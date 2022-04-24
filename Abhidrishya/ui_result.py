# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Result_pageTLAVkm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(613, 548)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 621, 571))
        self.frame.setStyleSheet(u"background-color: rgb(27, 26, 23);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 0, 151, 101))
        self.label.setStyleSheet(u"background-image: url(Abhidrishya/Abhidrishya_logo.png);")
        self.label.setPixmap(QPixmap(u"Abhidrishya/Abhidrishya_logo.png"))
        self.label.setScaledContents(True)
        self.Query_lbl = QLabel(self.frame)
        self.Query_lbl.setObjectName(u"Query_lbl")
        self.Query_lbl.setGeometry(QRect(80, 120, 171, 171))
        self.Query_lbl.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Query_lbl.setAlignment(Qt.AlignCenter)
        self.Result_lbl = QLabel(self.frame)
        self.Result_lbl.setObjectName(u"Result_lbl")
        self.Result_lbl.setGeometry(QRect(360, 120, 171, 171))
        self.Result_lbl.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Result_lbl.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 380, 101, 31))
        self.label_2.setStyleSheet(u"font: 75 16pt \"Gill Sans MT\";\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 420, 101, 31))
        self.label_3.setStyleSheet(u"font: 75 16pt \"Gill Sans MT\";\n"
"color: rgb(255, 255, 255);")
        self.name_lbl = QLabel(self.frame)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setGeometry(QRect(330, 380, 151, 31))
        self.name_lbl.setStyleSheet(u"font: 75 16pt \"Gill Sans MT\";\n"
"color: rgb(255, 255, 255);")
        self.age_lbl = QLabel(self.frame)
        self.age_lbl.setObjectName(u"age_lbl")
        self.age_lbl.setGeometry(QRect(330, 420, 151, 31))
        self.age_lbl.setStyleSheet(u"font: 75 16pt \"Gill Sans MT\";\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 320, 211, 31))
        self.label_6.setStyleSheet(u"font: 75 16pt \"Gill Sans MT\";\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.Query_lbl.setText("")
        self.Result_lbl.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name  :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Age     :", None))
        self.name_lbl.setText(QCoreApplication.translate("MainWindow", u"Pavan Kumar", None))
        self.age_lbl.setText(QCoreApplication.translate("MainWindow", u"96", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Details Of the Match", None))
    # retranslateUi

