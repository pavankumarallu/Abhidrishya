import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from Upload_page import *
from result_display import *
from mimetypes import init
import threading
import cv2
import os
import time

class Upload_check():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_query_image_lbl()
        self.ui.setupUi(self.main_win)
        
        
        self.query_file = ""
        self.result_file = ""
        self.ui.upload_btn.clicked.connect(self.upload_image)
        self.ui.match_btn.clicked.connect(self.check_image)
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(6000)
        
        
    
    def check_image(self):

        Dataset_path = "E:/CV/Real"
        sample = cv2.imread(self.query_file)
        t1 = threading.Thread(target=self.Finger_Match, name='t1')
        t2 = threading.Thread(target=self.check,name = 't2')
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        self.res_win.show()
        self.main_win.hide()
    
    def check(self):
        for i in range(6000):
            time.sleep(0.01)
            self.ui.progressBar.setValue(i+1)
        
        
        
    def Finger_Match(self):
        best_score = 0
        filename = None
        image = None
        kp1,kp2,mp = None,None,None
        Dataset_path = "E:/CV/Real"
        sample = cv2.imread(self.query_file)

        n = 0
        for file in [file for file in os.listdir(Dataset_path)]:
            n = n+1
            print(n)
            fingerprint_image = cv2.imread(Dataset_path+"/"+file)
            sift = cv2.SIFT_create()
            keypoints_1,description_1 = sift.detectAndCompute(sample,None)
            keypoints_2,description_2 = sift.detectAndCompute(fingerprint_image,None)
            matches = cv2.FlannBasedMatcher({'algorithm':1,'trees':10},{}).knnMatch(description_1,description_2,k = 2)
            match_points = []

            for p,q in matches:

                if p.distance < 0.1 * q.distance:
                    match_points.append(p)
            
            keypoints = 0
            if len(keypoints_1) < len(keypoints_2):
                keypoints = len(keypoints_1)
            else:
                keypoints = len(keypoints_2)
            if (len(match_points)/keypoints)*100 > best_score:
                best_score = len(match_points) / keypoints*100
                filename = file
                image = fingerprint_image
                kp1,kp2,mp = keypoints_1,keypoints_2,match_points
        self.result_file = filename
        self.res_win = result_show(self.query_file,self.result_file)
           
       
    def upload_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options,
        )
        pixmap = QtGui.QPixmap(fileName)
        self.ui.label_2.setPixmap(pixmap)
        self.query_file = fileName
        
    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Upload_check()
    window.show()
    sys.exit(app.exec_())