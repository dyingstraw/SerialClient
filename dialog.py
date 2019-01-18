# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Ui_Dialog(QMainWindow):
    def __init__(self):
        # pass
        # self.parent = parent
        super(Ui_Dialog,self).__init__()
        # self.setupUi(self)

    def accept(self):
        # print("accept")
        self.close()
    def reject(self):
        # print("reject")
        self.close()
    def setupUi(self, Dialog):
        Dialog.setObjectName("提示")
        Dialog.resize(662, 345)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowOpacity(0.8)
        # Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        # self.btn1 = QPushButton(Dialog)
        # self.btn1.setGeometry(QtCore.QRect(0, 250, 201, 41))
        # self.btn1.setText("hhhhhhh")
        # self.setBtnQss(self.btn1,"#34495E", "#FFFFFF", "#4E6D8C", "#F0F0F0", "#2D3E50", "#B8C6D1")


        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(390, 250, 201, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.msg = QtWidgets.QLabel(Dialog)
        self.msg.setGeometry(QtCore.QRect(0, 100, 621, 51))
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.timeBar = QtWidgets.QProgressBar(Dialog)
        self.timeBar.setGeometry(QtCore.QRect(110, 190, 471, 21))
        self.timeBar.setProperty("value", 100)
        self.timeBar.setObjectName("timeBar")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.msg.setText(_translate("Dialog", "提示：这是一个提示框"))

        # self.setBtnQss("#34495E", "#FFFFFF", "#4E6D8C", "#F0F0F0", "#2D3E50", "#B8C6D1")
    def timeProgress(self):
        
        if(self.timeBar.value()<=10):
            self.reject()
            self.t1.stop()
        else:
            self.timeBar.setValue(self.timeBar.value()-self.rate)
    def msgBox(self,seconds,msg):
        self.rate = int(10/seconds)      
     
        self.setupUi(self)
        
        

        self.t1=QTimer()
        self.t1.timeout.connect(self.timeProgress)
        self.t1.start(100)
        self.show()
        _translate = QtCore.QCoreApplication.translate
        self.msg.setText(_translate("Dialog",msg))
        # self.app.exec_()
        return 0
    def  setBtnQss(self,btn,normalColor,normalTxtColor,hoverColor,hoverTxtColor,pressedColor,pressedTxtColor):
        qss=""
        qss+="QPushButton{border-style:none;padding:10px;border-radius:5px;color:%s;background:%s;}"%(normalTxtColor,normalTxtColor)
        qss+="QPushButton:hover{color:%s;background:%s;}"%(hoverTxtColor,hoverColor)
        qss+="QPushButton:pressed{color:%s;background:%s;}"%(pressedTxtColor,pressedColor)
        btn.setStyleSheet(qss)



def msgBox(seconds,msg):
    app = QApplication(sys.argv)
    dlg=Ui_Dialog()
    dlg.show()
    app.exec_()
    # return dlg.msgBox(seconds,msg)
if __name__ == "__main__":
    # dlg=Ui_Dialog()
    app = QApplication(sys.argv)
    w = Ui_Dialog()
    w.msgBox(3,"hahahahha")
    sys.exit(app.exec_())