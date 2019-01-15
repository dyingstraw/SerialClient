from concurrent.futures import ThreadPoolExecutor
import serialThread
import time, threading
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainWindows import Ui_MainWindow
from cameraThread import CameraThread
from serialThread import SerialThread
from requestThread import RequestThread
from uploadThread import UploadThread
import random


class mainExec(QObject):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        # 有人 1-4 人脸识别 面部 舌苔
        self.finishFlag = [0, 0, 0, 0, 0, 0, 0, 0]
        self.allFinnish = False
        self.ticeFlag = False
        self.serial = SerialThread("com2")
        self.camera = CameraThread(0)
        self.shetaiCount = 0
        # 体检数据存储在这里
        self.heathData = {
            "mid": "0",
            "shengao": 0,
            "tizhong": 0,
            "tiwen": 0,
            "xinlv": 0
        }

        super(mainExec, self).__init__()

    def createUserHealth(self, instr):
        r = (bytes(instr[5], "utf-8")[0] - b"0" [0]) * 100
        r += (bytes(instr[6], "utf-8")[0] - b"0" [0]) * 10
        r += (bytes(instr[7], "utf-8")[0] - b"0" [0]) * 1
        r += (bytes(instr[8], "utf-8")[0] - b"0" [0]) * 0.1
        r += (bytes(instr[9], "utf-8")[0] - b"0" [0]) * 0.01
        return r

    def serialProgress(self, instr):
        # 0 有人
        # 1 身高
        # 2 体重
        # 3 体温
        # 4 心率
        # global ticeFlag
        # global finishFlag
        str = instr
        if len(instr) == 0:
            return
        # 第0步：单片机制动开始测量
        if str[4] == "0" and str[5] == "1":
            self.ticeFlag = True
            # 检测到有人就开始了，发送指令，让单片机自由测量
            self.serial.send("##SC500000\r\n")
        # 单片机主动关闭测量
        if str[4] == "0" and str[5] == "0":
            self.ticeFlag = False
        # print("ssssss:"+str)

        if instr[3] != 'E' and self.ticeFlag == True:
            if instr[4] == '1':
                self.finishFlag[1] = 1
                value = self.createUserHealth(str)
                self.ui.lcdNumber_shengao.setProperty("value", value)
                self.heathData['shengao'] = value
            if instr[4] == '2':
                self.finishFlag[2] = 1
                value = self.createUserHealth(str)
                self.heathData['tizhong'] = value
                self.ui.lcdNumber_tizhong.setProperty("value", value)
            if instr[4] == '3':
                self.finishFlag[3] = 1
                value = self.createUserHealth(str)
                self.heathData['tiwen'] = value
                self.ui.lcdNumber_tiwen.setProperty("value", value)
            if instr[4] == '4':
                self.finishFlag[4] = 1
                value = self.createUserHealth(str)
                self.heathData['xinlv'] = value
                self.ui.lcdNumber_xinlv.setProperty("value", value)

        # 测量完成(主动动判断)
        if sum(self.finishFlag) == 4:
            self.serial.send("##SCF00000\r\n")
            self.ticeFlag = False
            self.finishFlag = [0, 0, 0, 0, 0, 0, 0, 0]

            # 捕捉舌苔

            # 设置提示可见
            self.ui.label_tips.setVisible(True)
            self.timerShetai = QTimer(self)

            self.timerShetai.timeout.connect(self.shotShetai)
            self.timeId = self.timerShetai.start(1000)

    def uploadProgress(self, str):
        # 告诉单片机体检流程全部结束
        self.serial.send("##SC500003\r\n")
        print(str)

    def shotShetai(self):
        # global shetaiCount,timerShetai
        self.shetaiCount += 1
        font = QtGui.QFont()
        font.setPointSize(100)
        self.ui.label_tips.setFont(font)
        self.ui.label_tips.setText(str(5 - self.shetaiCount))
        self.camera.setMode("shetai" + str(self.shetaiCount))
        # 正在测舌苔
        self.serial.send("##SC500002\r\n")
        if (self.shetaiCount > 5):
            self.timerShetai.stop()
            # 体检结束结束
            self.serial.send("##SC500003\r\n")
            # 提交上传线程
            upload = UploadThread()
            upload.setData(self.heathData)
            upload._signal.connect(self.uploadProgress)
            upload.start()

            self.shetaiCount = 0
            font = QtGui.QFont()
            font.setPointSize(26)
            self.ui.label_tips.setFont(font)
            self.ui.label_tips.setVisible(False)

    def cameraProgress(self, str):
        jpg = QtGui.QPixmap(str).scaled(self.ui.label_Video.width(),
                                        self.ui.label_Video.height())
        self.ui.label_Video.setPixmap(jpg)
        # ui.lcdNumber_shengao.setProperty("value", random.random())
    def getUserinfo1(self, result):
        self.ui.lineEdit_Name.setText(result["userName"])
        self.ui.lineEdit_ID.setText(result["userId"])
        self.ui.textEdit_Other.setText(result["result"])

    # 按钮按下事件回调函数
    def getUserinfo(self):
        self.camera.setMode("detect")
        # 第2步：正在测面部以及识别个人信息
        self.serial.send("##SC500001\r\n")
        self.re = RequestThread()
        self.re._signal.connect(self.getUserinfo1)
        self.re.start()

        # ui.lineEdit_Name.setText("曹红伟")

    def main(self):

        #     启动相机0线程
        #     camera = CameraThread(0)
        self.camera._signal.connect(self.cameraProgress)
        self.camera.start()
        #     启动串口线程,波特率105200，串口2
        #     serial = SerialThread("com2")
        self.serial._signal.connect(self.serialProgress)
        self.serial.start()

        # 注册鼠标点击事件
        self.ui._clickedSignal.connect(self.getUserinfo)

        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    exec_main = mainExec()
    exec_main.main()