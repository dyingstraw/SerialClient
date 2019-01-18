# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
class Ui_MainWindow(QObject):
    _clickedSignal = pyqtSignal()
    def onClick(self):
        self._clickedSignal.emit()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("健康一体机")
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet("/*All Button Style*/\n"
"\n"
"QPushButton {\n"
"    font-size: 17px;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    min-width: 150px;\n"
"    min-height: 45px;\n"
"    background-color: #bdc3c7;\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: #cacfd2;\n"
"    background-color: #cacfd2;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-color: #a1a6a9;\n"
"    background-color: #a1a6a9;\n"
"}\n"
"QPushButton[enabled=\"false\"] {\n"
"    border-color: #1abc9c;\n"
"    background-color: #bdc3c7;\n"
"}\n"
"/*Default Button Style*/\n"
"\n"
"QPushButton[default=\"true\"] {\n"
"    background-color: #bdc3c7;\n"
"}\n"
"QPushButton[default=\"true\"]:hover {\n"
"    border-color: #cacfd2;\n"
"    background-color: #cacfd2;\n"
"}\n"
"QPushButton[default=\"true\"]:pressed {\n"
"    border-color: #a1a6a9;\n"
"    background-color: #a1a6a9;\n"
"}\n"
"/*Primary Button Style*/\n"
"\n"
"QPushButton[primary=\"true\"] {\n"
"    background-color: #1abc9c;\n"
"}\n"
"QPushButton[primary=\"true\"]:hover {\n"
"    border-color: #48c9b0;\n"
"    background-color: #48c9b0;\n"
"}\n"
"QPushButton[primary=\"true\"]:pressed {\n"
"    border-color: #16a085;\n"
"    background-color: #16a085;\n"
"}\n"
"/*Warning Button Style*/\n"
"\n"
"QPushButton[warning=\"true\"] {\n"
"    background-color: #f1c40f;\n"
"}\n"
"QPushButton[warning=\"true\"]:hover {\n"
"    border-color: #f4d313;\n"
"    background-color: #f4d313;\n"
"}\n"
"QPushButton[warning=\"true\"]:pressed {\n"
"    border-color: #cda70d;\n"
"    background-color: #cda70d;\n"
"}\n"
"/*Danger Button Style*/\n"
"\n"
"QPushButton[danger=\"true\"] {\n"
"    background-color: #e74c3c;\n"
"}\n"
"QPushButton[danger=\"true\"]:hover {\n"
"    border-color: #ec7063;\n"
"    background-color: #ec7063;\n"
"}\n"
"QPushButton[danger=\"true\"]:pressed {\n"
"    border-color: #c44133;\n"
"    background-color: #c44133;\n"
"}\n"
"/*Success Button Style*/\n"
"\n"
"QPushButton[success=\"true\"] {\n"
"    background-color: #2ecc71;\n"
"}\n"
"QPushButton[success=\"true\"]:hover {\n"
"    border-color: #58d68d;\n"
"    background-color: #58d68d;\n"
"}\n"
"QPushButton[success=\"true\"]:pressed {\n"
"    border-color: #27ad60;\n"
"    background-color: #27ad60;\n"
"}\n"
"/*Inverse Button Style*/\n"
"\n"
"QPushButton[inverse=\"true\"] {\n"
"    background-color: #34495e;\n"
"}\n"
"QPushButton[inverse=\"true\"]:hover {\n"
"    border-color: #415b76;\n"
"    background-color: #415b76;\n"
"}\n"
"QPushButton[inverse=\"true\"]:pressed {\n"
"    border-color: #2c3e50;\n"
"    background-color: #2c3e50;\n"
"}\n"
"/*Info Button Style*/\n"
"\n"
"QPushButton[info=\"true\"] {\n"
"    background-color: #3498db;\n"
"}\n"
"QPushButton[info=\"true\"]:hover {\n"
"    border-color: #5dade2;\n"
"    background-color: #5dade2;\n"
"}\n"
"QPushButton[info=\"true\"]:pressed {\n"
"    border-color: #2c81ba;\n"
"    background-color: #2c81ba;\n"
"}\n"
"/*All QLineEdit*/\n"
"\n"
"QLineEdit {\n"
"    min-width: 180px;\n"
"    min-height: 35px;\n"
"    font-family: \"Lato\", Helvetica, Arial, sans-serif;\n"
"    font-size: 15px;\n"
"    color: #34495e;\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 6px;\n"
"}\n"
"QLineEdit:focus {\n"
"    outline: 0;\n"
"    border-color: #1abc9c;\n"
"}\n"
"QLineEdit[echoMode=\"2\"],\n"
"QLineEdit[echoMode=\"3\"] {\n"
"    lineedit-password-character: 42;\n"
"}\n"
"QLineEdit[enabled=\"false\"] {\n"
"    color: #d5dbdb;\n"
"    border: 2px solid #d5dbdb;\n"
"    background-color: #f4f6f6;\n"
"    cursor: default;\n"
"    opacity: 0.7;\n"
"}\n"
"/*Search QLineEdit*/\n"
"\n"
"QLineEdit[search-left=\"true\"] {\n"
"    padding-left: 24px;\n"
"    background: url(qsslib/img/search.png) no-repeat center left;\n"
"}\n"
"QLineEdit[search-right=\"true\"] {\n"
"    padding-right: 24px;\n"
"    background: url(qsslib/img/search.png) no-repeat center right;\n"
"}\n"
"/*Error QLineEdit*/\n"
"\n"
"QLineEdit[error=\"true\"] {\n"
"    color: #e74c3c;\n"
"    border: 2px solid #e74c3c;\n"
"}\n"
"QLineEdit[error=\"true\"]:focus {\n"
"    outline: 0;\n"
"}\n"
"/*Success QLineEdit*/\n"
"\n"
"QLineEdit[success=\"true\"] {\n"
"    color: #2ecc71;\n"
"    border: 2px solid #2ecc71;\n"
"}\n"
"QLineEdit[success=\"true\"]:focus {\n"
"    outline: 0;\n"
"}\n"
"/*QComboBox Style*/\n"
"\n"
"QComboBox {\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    min-width: 80px;\n"
"    min-height: 30px;\n"
"    background-color: #1abc9c;\n"
"}\n"
"QComboBox::drop-down {\n"
"    width: 25px;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    color: #00ff00;\n"
"    border-style: solid;\n"
"    border-width: 8px 6px;\n"
"}\n"
"\n"
"/*Page List Widget Style*/\n"
"QPushButton#_previous_btn,QPushButton#_next_btn {\n"
"    max-width: 49px;\n"
"    max-height: 39px;\n"
"    min-width: 49px;\n"
"    min-height: 39px;\n"
"    width: 49px;\n"
"    height: 39px;\n"
"    border-color: #E4E7EA;\n"
"    \n"
"}\n"
"QPushButton#_previous_btn:hover,QPushButton#_next_btn:hover {\n"
"    border-color: #1ABC9C;\n"
"    background-color: #1ABC9C;\n"
"    \n"
"}\n"
"QPushButton#_previous_btn:pressed,QPushButton#_next_btn:pressed {\n"
"    border-color: #1ABC9C;\n"
"    background-color: #1ABC9C;\n"
"    \n"
"}\n"
"QPushButton#_previous_btn {\n"
"    padding-right: 1px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 6px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background: #E4E7EA url(qsslib/img/arrow_left_white.png) no-repeat center center;\n"
"}\n"
"QPushButton#_next_btn {\n"
"    padding-left: 1px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: #E4E7EA url(qsslib/img/arrow_right_white.png) no-repeat center center;\n"
"}\n"
"\n"
"QListView#_page_list_widget {\n"
"    max-height: 40px;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QListView#_page_list_widget::item {\n"
"    margin: 1px;\n"
"    color: white;\n"
"    background-color: #E4E7EA;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QListView#_page_list_widget::item:selected {\n"
"    background-color: #1ABC9C;\n"
"}\n"
"QListView#_page_list_widget::item:focus {\n"
"    background-color: #1ABC9C;\n"
"}\n"
"\n"
"QListView#_page_list_widget::item:hover {\n"
"    background-color: #1ABC9C;\n"
"}\n"
"\n"
"/*QScrollBar Style*/\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"    padding-top: 12px;\n"
"    padding-bottom: 12px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"    padding-left: 12px;\n"
"    padding-right: 12px;\n"
"}\n"
"\n"
"QScrollBar:vertical:hover,QScrollBar:horizontal:hover {\n"
"    background: rgba(0, 0, 0, 30);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(0, 0, 0, 50);\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(0, 0, 0, 50);\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar::add-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar::sub-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 12px;\n"
"    width: 10px;\n"
"    background: transparent;\n"
"    subcontrol-position: top;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    height: 10px;\n"
"    width: 12px;\n"
"    background: transparent;\n"
"    subcontrol-position: left;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"    image: url(qsslib/img/scrollbar_arrowup_normal.png);\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"    image: url(qsslib/img/scrollbar_arrowleft_normal.png);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:hover {\n"
"    image: url(qsslib/img/scrollbar_arrowup_down.png);\n"
"}\n"
"QScrollBar::left-arrow:horizontal:hover {\n"
"    image: url(qsslib/img/scrollbar_arrowleft_down.png);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"    image: url(qsslib/img/scrollbar_arrowup_highlight.png);\n"
"}\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"    image: url(qsslib/img/scrollbar_arrowleft_highlight.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 12px;\n"
"    width: 10px;\n"
"    background: transparent;\n"
"    subcontrol-position: bottom;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    height: 10px;\n"
"    width: 12px;\n"
"    background: transparent;\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"    image: url(qsslib/img/scrollbar_arrowdown_normal.png);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    image: url(qsslib/img/scrollbar_arrowright_normal.png);\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:hover {\n"
"    image: url(qsslib/img/scrollbar_arrowdown_down.png);\n"
"}\n"
"QScrollBar::right-arrow:horizontal:hover {\n"
"    image: url(qsslib/img/scrollbar_arrowright_down.png);\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"    image: url(qsslib/img/scrollbar_arrowdown_highlight.png);\n"
"}\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"    image: url(qsslib/img/scrollbar_arrowright_highlight.png);\n"
"}\n"
"\n"
"/*QProgressBar Style*/\n"
"QProgressBar{\n"
"    height: 12px;\n"
"    background: #ebedef;\n"
"    border-radius: 6px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 6px;\n"
"    background: #1abc9c;\n"
"}\n"
"\n"
"/*QSlider*/\n"
"QSlider::groove:horizontal {\n"
"    height: 12px;\n"
"    background: #ebedef;\n"
"    border-radius: 6px;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 12px;\n"
"    background: #ebedef;\n"
"    border-radius: 6px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #1abc9c;\n"
"    height: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: #1abc9c;\n"
"    width: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #16a085;\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    margin-top: -3px;\n"
"    margin-bottom: -3px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #16a085;\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    margin-left: -3px;\n"
"    margin-right: -3px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover,QSlider::handle:horizontal:hover {\n"
"    background: #48c9b0;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato,Helvetica,Arial,sans-serif")
        font.setPointSize(-1)
        self.lineEdit_Name.setFont(font)
        self.lineEdit_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.horizontalLayout_2.addWidget(self.lineEdit_Name)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato,Helvetica,Arial,sans-serif")
        font.setPointSize(-1)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.horizontalLayout_3.addWidget(self.lineEdit_ID)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_Sex = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato,Helvetica,Arial,sans-serif")
        font.setPointSize(-1)
        self.lineEdit_Sex.setFont(font)
        self.lineEdit_Sex.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Sex.setObjectName("lineEdit_Sex")
        self.horizontalLayout_4.addWidget(self.lineEdit_Sex)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.textEdit_Other = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Other.setObjectName("textEdit_Other")
        self.horizontalLayout_5.addWidget(self.textEdit_Other)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.pushButton_getinfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getinfo.setParent(self.centralwidget)
        self.pushButton_getinfo.setMinimumSize(QtCore.QSize(150, 45))
        self.pushButton_getinfo.setObjectName("pushButton_getinfo")
        self.verticalLayout_7.addWidget(self.pushButton_getinfo)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_Video = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Video.sizePolicy().hasHeightForWidth())
        self.label_Video.setSizePolicy(sizePolicy)
        self.label_Video.setMinimumSize(QtCore.QSize(600, 500))
        self.label_Video.setMaximumSize(QtCore.QSize(600, 500))
        self.label_Video.setAutoFillBackground(False)
        self.label_Video.setStyleSheet("\n"
"boder:1px\n"
"")
        self.label_Video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_Video.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Video.setObjectName("label_Video")
        self.horizontalLayout_6.addWidget(self.label_Video)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber_xinlv = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_xinlv.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber_xinlv.setSmallDecimalPoint(True)
        self.lcdNumber_xinlv.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_xinlv.setProperty("value", 0.0)
        self.lcdNumber_xinlv.setProperty("intValue", 0)
        self.lcdNumber_xinlv.setObjectName("lcdNumber_xinlv")
        self.verticalLayout.addWidget(self.lcdNumber_xinlv)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber_tiwen = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_tiwen.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber_tiwen.setSmallDecimalPoint(True)
        self.lcdNumber_tiwen.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_tiwen.setProperty("value", 0.0)
        self.lcdNumber_tiwen.setProperty("intValue", 0)
        self.lcdNumber_tiwen.setObjectName("lcdNumber_tiwen")
        self.verticalLayout_2.addWidget(self.lcdNumber_tiwen)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lcdNumber_shengao = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_shengao.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber_shengao.setSmallDecimalPoint(True)
        self.lcdNumber_shengao.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_shengao.setProperty("value", 0.0)
        self.lcdNumber_shengao.setProperty("intValue", 0)
        self.lcdNumber_shengao.setObjectName("lcdNumber_shengao")
        self.verticalLayout_3.addWidget(self.lcdNumber_shengao)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lcdNumber_tizhong = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_tizhong.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber_tizhong.setSmallDecimalPoint(True)
        self.lcdNumber_tizhong.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_tizhong.setProperty("value", 0.0)
        self.lcdNumber_tizhong.setProperty("intValue", 0)
        self.lcdNumber_tizhong.setObjectName("lcdNumber_tizhong")
        self.verticalLayout_4.addWidget(self.lcdNumber_tizhong)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lcdNumber_timer = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_timer.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber_timer.setSmallDecimalPoint(True)
        self.lcdNumber_timer.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_timer.setProperty("value", 0.0)
        self.lcdNumber_timer.setProperty("intValue", 0)
        self.lcdNumber_timer.setObjectName("lcdNumber_timer")
        self.verticalLayout_5.addWidget(self.lcdNumber_timer)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_getinfo.clicked.connect(self.onClick)
        self.label_tips = QtWidgets.QLabel(MainWindow)

        self.label_tips.setGeometry(QtCore.QRect(0, 0, 591, 421))
        self.label_tips.setAutoFillBackground(True)

        self.label_tips.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_tips.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tips.setObjectName("label_tips")
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_tips.setFont(font)
        self.label_tips.setText(">>即将采集舌苔，倒计时5秒<<")
        self.label_tips.setVisible(False)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "个人信息"))
        self.label_7.setText(_translate("MainWindow", "姓名："))
        self.label_8.setText(_translate("MainWindow", "编号："))
        self.label_9.setText(_translate("MainWindow", "性别："))
        self.label_10.setText(_translate("MainWindow", "备注："))
        self.pushButton_getinfo.setText(_translate("MainWindow", "人脸识别"))
        self.label_Video.setText(_translate("MainWindow", "No Signle"))
        self.label.setText(_translate("MainWindow", "心率"))
        self.label_2.setText(_translate("MainWindow", "体温"))
        self.label_3.setText(_translate("MainWindow", "身高"))
        self.label_4.setText(_translate("MainWindow", "体重"))
        self.label_5.setText(_translate("MainWindow", "倒计时"))

