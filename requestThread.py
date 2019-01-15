from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
from requests_toolbelt import MultipartEncoder
import requests


class RequestThread(QThread):
    _signal = pyqtSignal(dict)

    def __init__(self):

        super(RequestThread, self).__init__()

    def run(self):
        # shuiyihui
        self.sleep(1)
        m = MultipartEncoder(
            fields={
                "tokenId":
                "2NyNzJ2dKD00CuKi9=DmrxxCyD2t465QSKTYEd9LWhhlXVY0IXyr1HC)VigGIiN0udMB7q_S21itgC4t56gMwfz5RUghoiQKtPWxiihKkc8NGULrh_aH_LBv375QM)OwGHANIvXKvxggOPmx7jwzfOq55=CUGJRiWEp8KStuK23L0800k=lqSrcSs1XJlRlOtBZXlXQb7445",
                "userGroup":
                "default",
                "file": ('temp_detect.jpg', open("temp/temp_detect.jpg", 'rb'),
                         'image/jpeg')  #mmexport1541509631472.jpg
            })
        url = "https://api.mybcfuture.com/ns/face"

        response = requests.post(
            url, data=m, headers={'Content-Type': m.content_type},
            timeout=10)  #files=files0
        try:
            faceDict = json.loads(response.text)
            print(faceDict)
            if faceDict['code'] == '3000':
                try:
                    userIdDict = json.loads(faceDict['result'])
                    print("%s %s" % (userIdDict['userId'],
                                     userIdDict['userName']))
                    # ui.lineEdit_Name.setText(userIdDict['userName'])
                    # self._signal.emit(userIdDict)
                except:
                    self._signal.emit({
                        "userId": "###",
                        "userName": "#######",
                        "result": "Error"
                    })
                    print("json errorr")
                    raise
                # raise  Exception("json error")
                try:
                    scoreDict = json.loads(userIdDict['result'])
                    print(scoreDict['score'])
                    if scoreDict['score'] < 60:
                        self._signal.emit({
                            "userId": "###",
                            "userName": "#######",
                            "result": "Error"
                        })
                        print("errphoto2")
                    else:
                        self._signal.emit(userIdDict)
                        print('photook')
                except:
                    self._signal.emit({
                        "userId": "###",
                        "userName": "#######",
                        "result": "Error"
                    })
                    print("error json")

            else:
                self._signal.emit({
                    "userId": "###",
                    "userName": "#######",
                    "result": "Error"
                })
                print("errphoto1")
        except:
            self._signal.emit({
                "userId": "###",
                "userName": "#######",
                "result": "Error"
            })
            print("ssss")