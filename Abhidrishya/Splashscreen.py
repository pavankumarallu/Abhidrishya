# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplachscreenFlvyel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(540, 352)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(27, 26, 23);\n"
"	color:rgb(220,220,220);\n"
"	border-radius:20px;\n"
"}")
        self.DropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.DropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 60, 151, 111))
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
        self.progressBar = QProgressBar(self.DropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 220, 371, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	font: 75 11pt \"Times New Roman\";\n"
"color: rgb(0,0,0);\n"
"border-style : none;\n"
"border-radius:8px;\n"
"text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.159, y1:1, x2:1, y2:0, stop:0 rgba(240, 165, 0, 255), stop:1 rgba(255, 212, 142, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_2 = QLabel(self.DropShadowFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 250, 511, 21))
        self.label_2.setStyleSheet(u"font: 11pt \"OCR A Extended\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.DropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"Loading....", None))
    # retranslateUi

