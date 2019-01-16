import serial, threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from public import PUBLIC

class SerialThread(QThread):

    _signal = pyqtSignal(str)
    _signalError = pyqtSignal(dict)

    def __init__(self, comName):
        super(SerialThread, self).__init__()
        # self._signalError.emit(PUBLIC.SERIAL_OPEN_ERROR)
        try:
            self.ser = serial.Serial(comName, baudrate=115200, timeout=0.1)
            print("worked in ", self.ser.portstr)
        except Exception as e:
            raise e
        
        
        

    def run(self):
        print("serialThread is running!")
        while (True):
            data = self.ser.readline()
            if len(data) != 0:
                # 校验数据
                if data[0] == b"#" [0] and data[1] == b"#" [0]:
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

    def send(self, data):
        self.ser.write(data.encode("utf-8"))


if __name__ == "__main__":
    ser = SerialThread("com2")
    ser.run()