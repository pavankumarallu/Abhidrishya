import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *



from ui_result import *
# from finger import find_match
from dbCodes import CriminalRecord

class result_show():
    def __init__(self,query,result):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.query = query
        self.result = "E:/CV/Real/"+result
        pixmap_1 = QtGui.QPixmap(self.query)
        pixmap_2 = QtGui.QPixmap(self.result)
        print(result)
        self.ui.Query_lbl.setPixmap(pixmap_1)
        self.ui.Result_lbl.setPixmap(pixmap_2)
        self.Criminal = CriminalRecord(result)
        res = self.Criminal.fetch_name_age()
        self.ui.name_lbl.setText(str(res[0][0]))
        self.ui.age_lbl.setText(str(res[0][1]))
        
    def show(self):
        self.main_win.show()