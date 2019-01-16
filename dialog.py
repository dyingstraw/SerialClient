# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(662, 345)
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
        self.timeBar.setProperty("value", 24)
        self.timeBar.setObjectName("timeBar")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.msg.setText(_translate("Dialog", "提示：这是一个提示框"))
    def msgBox(self,time,msg):
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = QtWidgets.Dialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.MainWindow)
        self.dialog.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    dlg=Ui_Dialog()
    dlg.msgBox(5,"sss")