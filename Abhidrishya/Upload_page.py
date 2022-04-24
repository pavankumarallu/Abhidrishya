# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Upload_pageAQqmFx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Ui_query_image_lbl(object):
    def setupUi(self, query_image_lbl):
        if not query_image_lbl.objectName():
            query_image_lbl.setObjectName(u"query_image_lbl")
        query_image_lbl.resize(613, 490)
        query_image_lbl.setStyleSheet(u"background-color: rgb(27, 26, 23);")
        self.centralwidget = QWidget(query_image_lbl)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(27, 26, 23);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.upload_btn = QPushButton(self.frame)
        self.upload_btn.setObjectName(u"upload_btn")
        self.upload_btn.setGeometry(QRect(220, 10, 151, 41))
        self.upload_btn.setStyleSheet(u"background-color: rgb(240, 165, 0);\n"
"font: 75 18pt \"Goudy Old Style\";")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 101, 81))
        self.label.setStyleSheet(u"background-image: url(Abhidrishya/Abhidrishya_logo.png);")
        self.label.setPixmap(QPixmap(u"Abhidrishya/Abhidrishya_logo.png"))
        self.label.setScaledContents(True)
        self.match_btn = QPushButton(self.frame)
        self.match_btn.setObjectName(u"match_btn")
        self.match_btn.setGeometry(QRect(230, 340, 151, 41))
        self.match_btn.setStyleSheet(u"background-color: rgb(240, 165, 0);\n"
"font: 75 18pt \"Goudy Old Style\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 130, 311, 171))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(190, 410, 251, 23))
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.frame)

        query_image_lbl.setCentralWidget(self.centralwidget)

        self.retranslateUi(query_image_lbl)

        QMetaObject.connectSlotsByName(query_image_lbl)
    # setupUi

    def retranslateUi(self, query_image_lbl):
        query_image_lbl.setWindowTitle(QCoreApplication.translate("query_image_lbl", u"MainWindow", None))
        self.upload_btn.setText(QCoreApplication.translate("query_image_lbl", u"Upload", None))
        self.label.setText("")
        self.match_btn.setText(QCoreApplication.translate("query_image_lbl", u"Find match", None))
        self.label_2.setText("")
    # retranslateUi

