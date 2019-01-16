from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import random
import threading
from public import PUBLIC
class CameraThread(QThread):
    #定义信号,定义参数为str类型
    _signal = pyqtSignal(str)
    _signalError = pyqtSignal(dict)

    lock = threading.Lock()

    def __init__(self, devid):
        self.devid = devid
        # modes :runtime detect face shetai
        self.mode = "runtime"
        super(CameraThread, self).__init__()

    def run(self):
        self.camera()

    def camera(self):
        cap = cv2.VideoCapture(self.devid)
        if cap==None:
            self._signalError.connect(PUBLIC.CAMERA_OPEN_ERROR)
            return
        # i = 0
        while (True):
            _, frame = cap.read()
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # i = i + 1
            # i = i % 100
            # cv2.putText(frame,"read:"+str(result),(10,500), font, 4,(255,0,255),2,cv2.LINE_AA)
            # cv2.imwrite("temp/temp"+str(i)+".jpg",frame)
            # print("temp/temp_" + self.mode + ".jpg")
            # 加锁
            if self.lock.acquire():
                cv2.imwrite("temp/temp_" + self.mode + ".jpg", frame)
                if self.mode != "runtime":
                    print("mode:" + self.mode)
                    self.mode = "runtime"
                self.lock.release()
            else:
                print("没有获取锁")
            # cv2.imshow("video",frame)
            self._signal.emit("temp/temp_runtime" + ".jpg")

            cv2.waitKey(30)

    def setMode(self, mode):
        # modes :runtime detect face shetai
        # 加锁
        if (self.lock.acquire()):
            self.mode = mode
            self.lock.release()


if __name__ == "__main__":
    print("mian")
    cc = CameraThread(0)
    cc.run()