from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
from requests_toolbelt import MultipartEncoder
import requests
class UploadThread(QThread):
    _signal=pyqtSignal(str)
    def __init__(self):
        super(UploadThread,self).__init__()
    def setData(self,dict_):
        self.userHealthDict = dict_
    def run(self):
        print("upload begin")
        files00 = {
            "shetai"  : open("temp/temp_shetai1.jpg",'rb'),
            "shetai2" : open("temp/temp_shetai2.jpg",'rb'),
            "shetai3" : open("temp/temp_shetai3.jpg",'rb'),
            "shetai4" : open("temp/temp_shetai4.jpg",'rb'),
            "shetai5" : open("temp/temp_shetai5.jpg",'rb'),
            "mianbu"  : open("temp/temp_detect.jpg",'rb'),
        }
                
        datas={
            "tokenid":"001001",
            "mid":"0000072",
            "did":"00112",
            "xinlv":90,
            "xueyang":99,
            "tizhong":88,
            "tiwen1":77,
            "shengao":60,
        }
        datas['mid'] = self.userHealthDict['mid']
        datas['xinlv'] = self.userHealthDict['xinlv']
        datas['xueyang'] = 0
        datas['tizhong'] = self.userHealthDict['tizhong']
        datas['tiwen1'] = self.userHealthDict['tiwen']
        datas['shengao'] = self.userHealthDict['shengao']
        url = "http://herb.mybcfuture.com/index.php/Api/Reception/rec"
        response = requests.post(url, data=datas,files=files00)
        # 上传完成
        self._signal.emit(response.text)
        print("upload begin")
        print (response.text)
        