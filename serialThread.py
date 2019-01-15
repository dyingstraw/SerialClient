import serial,threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class SerialThread(QThread):

    _signal=pyqtSignal(str)
    def __init__(self,comName):
        self.ser = serial.Serial(comName,baudrate=115200,timeout=0.1)
        print("worked in ",self.ser.portstr)
        super(SerialThread,self).__init__()
    def run(self):
        print("serialThread is running!")
        while(True):
            data = self.ser.readline()
            if len(data)!=0:                
                # 校验数据
                if data[0]==b"#"[0] and data[1]==b"#"[0] :
                    # 校验成功
                    # self.ser.write("##RE000000\r\n".encode("utf-8"))
                    # 校验正确 将数据发送到主线程
                    self._signal.emit(bytes.decode(data))
                else:
                    # 校验错误
                    self.ser.write("##RE0FFFFF\r\n".encode("utf-8"))
                    self._signal.emit("##RE0FFFFF\r\n")
            else:
                # 如果没有数据
                self._signal.emit("")
    def send(self,data):
        self.ser.write(data.encode("utf-8"))
if __name__ == "__main__":
    ser = SerialThread("com2")
    ser.run()