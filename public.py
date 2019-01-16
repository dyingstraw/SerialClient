class PUBLIC:

    DEBUG = True

    TEST ={"code":0,"message":"test"}
    SUCCESS = {"code":0,"message":"SUCCESS"}
    NET_ERROR = {"code":1001,"message":"网络连接失败"}

    FACE_DETECT_ERROR = {"code":2001,"message":"人脸识别失败"}

    CAMERA_OPEN_ERROR = {"code":3001,"message":"摄像头打开失败，请查看是否有摄像头，或者摄像头已经被打开"}
    
    SERIAL_OPEN_ERROR ={
        "code":4001,
        "message":"串口打开失败"
        }
