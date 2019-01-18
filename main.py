import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
import serialThread
from cameraThread import CameraThread
from mainWindows_ui import Ui_MainWindow
from requestThread import RequestThread
from serialThread import SerialThread
from uploadThread import UploadThread
from dialog import Ui_Dialog as messageBox
import dialog 
import logging
# logging.basicConfig(filename="alog.log",filemode='a',level = logging.DEBUG,format = '%(filename)s in %(lineno)d Lines: %(threadName)s-%(thread)d, %(asctime)s - %(name)s - %(levelname)s:%(message)s')
# 不要有名字
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(filename)s in %(lineno)d Lines: %(threadName)s-%(thread)d, %(asctime)s - %(name)s - %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
# 使用FileHandler输出到文件
fh = logging.FileHandler('log.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
# 使用StreamHandler输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# 添加两个Handler
logger.addHandler(ch)
logger.addHandler(fh)


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
        self.timerShetai=QTimer(self)

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
            self.finishFlag[0] = 1
            logger.info("deprecated有人来了，发送##SC500000\r\n给单片机")
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
            # 单片机发送开始拍摄舌苔的指令 ##SC500002\r\n
            if instr[4] == '5' and instr[9]=='2' and instr[8]=='0':
                # 捕捉舌苔
                # 设置提示可见
                logger.info("收到舌苔指令")
                self.ui.label_tips.setVisible(True)
                logger.info(threading.currentThread().getName())
                # self.timerShetai = QTimer(self)
                self.timerShetai.timeout.connect(self.shotShetai)
                self.timerShetai.start(1000)
                logger.info(self.timerShetai)
                
        # 测量完成(主动动判断)
        if sum(self.finishFlag) == 8:
            logger.info("（deprecated）基础数据完成##SCF00000\r\n")
            self.serial.send("##SCF00000\r\n")
            # 提交上传线程
            self.upload = UploadThread()
            self.upload.setData(self.heathData)
            self.upload._signal.connect(self.uploadProgress)
            self.upload.start()

            self.ticeFlag = False
            self.finishFlag = [0, 0, 0, 0, 0, 0, 0, 0]

            # # 捕捉舌苔
            # # 设置提示可见
            # self.ui.label_tips.setVisible(True)
            # self.timerShetai = QTimer(self)

            # self.timerShetai.timeout.connect(self.shotShetai)
            # self.timeId = self.timerShetai.start(1000)

    def uploadProgress(self, str):
        # 告诉单片机体检流程全部结束
        # 上传结束
        logger.info("体检结束##SC500003\r\n")
        logger.info(str)
        result = json.loads(str)
        if result["errorcode"]!="1000":
            logger.info("上传失败，请重新体检##SC500004")
            self.serial.send("##SC500004\r\n")
            # messageBox.msgBox(3,"上传失败，请重新体检")
        else:
            logger.info("上传成功，体检结束##SC500003\r\n")
            self.serial.send("##SC500003\r\n")
            # messageBox.msgBox(3,"上传成功，体检结束")

        # qing 0
        self.ui.lineEdit_ID.setText("")
        self.ui.lineEdit_Name.setText("")
        self.ui.lineEdit_Sex.setText("")
        self.ui.textEdit_Other.setText("")
        self.ui.lcdNumber_xinlv.setProperty("value",0)
        self.ui.lcdNumber_tiwen.setProperty("value",0)
        self.ui.lcdNumber_shengao.setProperty("value",0)
        self.ui.lcdNumber_tizhong.setProperty("value",0)
        self.msgbox = messageBox()
        self.msgbox.msgBox(5,"体检结束")

    def shotShetai(self):
        # global shetaiCount,timerShetai
        self.shetaiCount += 1
        font = QtGui.QFont()
        font.setPointSize(100)
        self.ui.label_tips.setFont(font)
        self.ui.label_tips.setText(str(5 - self.shetaiCount))
        self.camera.setMode("shetai" + str(self.shetaiCount))
        # 正在测舌苔
        logger.info("To:正在测舌苔##SC500002\r\n")
        self.serial.send("##SC500002\r\n")
        if (self.shetaiCount > 5):
            logger.info(threading.currentThread().getName())
            try:
                # self.timerShetai.killTimer()
                # self.killTimer(self.timerShetai.timerId())
                self.timerShetai.stop()
            except Exception as e:
                logger.debug(e)
                raise e
            self.timerShetai.stop()
            # 告诉下位机拍摄舌苔完成
            logger.info("To:舌苔测量完成####SC500012\r\n")
            self.finishFlag[7]= 1
            self.serial.send("##SC500012\r\n")
            self.shetaiCount = 0

            if sum(self.finishFlag) == 8:
                logger.info("（deprecated）基础数据完成##SCF00000\r\n")
                self.serial.send("##SCF00000\r\n")
                # 提交上传线程
                self.upload = UploadThread()
                self.upload.setData(self.heathData)
                self.upload._signal.connect(self.uploadProgress)
                self.upload.start()

            self.ticeFlag = False
            self.finishFlag = [0, 0, 0, 0, 0, 0, 0, 0]

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
        # 人脸识别失败，发送##SC500021\r\n告诉单片机状态
        # 人脸识别成功，发送##SC500011\r\n告诉单片机状态
        self.msgbox = messageBox()
        self.msgbox.msgBox(3,"正在进行人脸识别，请稍后。。")
        # msgbox = messageBox()
        # msgbox.show()
        # dialog.msgBox(2,"w12121")
        # logger.info("人脸识别")
        if result["result"]=="Error":
            logger.info("To:人脸识别失败：##SC500021\r\n")
            self.serial.send("##SC500021\r\n")
            self.msgbox = messageBox()
            self.msgbox.msgBox(3,"人脸识别失败")
        else:
            # 置位脸部，人脸识别
            self.finishFlag[5] =1
            self.finishFlag[6] =1
            logger.info("To:人脸识别成功：##SC500011\r\n")
            self.serial.send("##SC500011\r\n")
            self.msgbox = messageBox()
            self.msgbox.msgBox(3,"人脸识别成功")
        # 显示人脸识别结果到界面
        self.ui.lineEdit_Name.setText(result["userName"])
        self.ui.lineEdit_ID.setText(result["userId"])
        self.ui.textEdit_Other.setText(result["result"])
        self.ui.pushButton_getinfo.setText("人脸识别")
        self.ui.pushButton_getinfo.setDisabled(False)

    # 按钮按下事件回调函数
    def getUserinfo(self):
        self.camera.setMode("detect")
        self.ui.pushButton_getinfo.setText("正在识别，请稍后...")
        self.ui.pushButton_getinfo.setDisabled(True)
        # msg_box = QMessageBox.information(self.MainWindow,"提示","hhhhhh")
        # print("12121:",msg_box)
        # 第2步：正在测面部以及识别个人信息
        logger.info("To:正在准备人脸识别：##SC500001\r\n")
        self.serial.send("##SC500001\r\n")
        self.re = RequestThread()
        self.re._signalError.connect(self.errorCallback)
        self.re._signal.connect(self.getUserinfo1)
        self.re.start()

        # ui.lineEdit_Name.setText("曹红伟")
    # 处理全局错误
    def errorCallback(self,message):
        self.msgbox = messageBox()
        self.msgbox.msgBox(3,str(message))
        logger.info("全局错误：" + message.__str__())        
        # print("全局错误：" + message.__str__())
    def main(self):
        #     启动相机0线程
        #     camera = CameraThread(0)
        self.camera._signal.connect(self.cameraProgress)
        self.camera.start()
        #     启动串口线程,波特率105200，串口2
        #     serial = SerialThread("com2")
        self.serial._signal.connect(self.serialProgress)
        # self.serial._signalError.connect(lambda x: print("全局错误：" ,x))
        self.serial.start()

        # 注册鼠标点击事件
        self.ui._clickedSignal.connect(self.getUserinfo)

        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    exec_main = mainExec()
    exec_main.main()
