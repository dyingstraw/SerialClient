from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import random
import threading
import time
import queue
from public import PUBLIC
from facedetect import FaceDetect
class CameraThread(QThread):
    #定义信号,定义参数为str类型
    _signal = pyqtSignal(str)
    _signalError = pyqtSignal(dict)
    _signalDetectFace = pyqtSignal(list)
    _signalMessage = pyqtSignal(str)

    lock = threading.Lock()

    def __init__(self, devid):
        self.devid = devid
        # modes :runtime detect face shetai
        self.mode = "runtime"
        self.faceFlag = False
        self.faceList =[-100,1200,100,200,-100]
        self.face = FaceDetect()
        self.faceStableStandar = 0
        self.faceCount =0
        super(CameraThread, self).__init__()

    def run(self):
        self.camera()

    def camera(self):
        cap = cv2.VideoCapture(self.devid)
        if cap==None:
            self._signalError.connect(PUBLIC.CAMERA_OPEN_ERROR)
            return
        # i = 0
        _, frame = cap.read()
        # 稳定因素
        self.faceStableStandar = frame.shape[0]/8
        beginTime =time.time()
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
                
                
                # 每隔0.5s检查一下有无人脸
                if time.time()-beginTime >= 0.5 and self.mode == "runtime" :
                    r=self.face.detect(frame,True)
                    if len(r)>0 and self.faceFlag==True:
                        # 如果人头接近静止
                        if self.isStable(r[0],self.faceStableStandar):              
                            self._signalDetectFace.emit(list(r))
                            self.faceFlag =False
                        else:
                            # print("not stable")
                            self._signalMessage.emit("don't move")
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
    def isStable(self,r,standar=100):
        self.faceCount +=1
        self.faceList[self.faceCount % 5] = r[0]+r[2]/2
        temp = self.faceList[:]
        temp.sort()
        if temp[-1]-temp[0] < standar:
            return True
        else:
            return False




        

    def setMode(self, mode):
        # modes :runtime detect face shetai
        # 加锁
        if (self.lock.acquire()):
            self.mode = mode
            self.lock.release()
    def setFaceFlag(self, f):
        # modes :runtime detect face shetai
        # 加锁
        if (self.lock.acquire()):
            self.faceFlag = f
            self.lock.release()


if __name__ == "__main__":
    print("mian")
    cc = CameraThread(0)
    cc.run()