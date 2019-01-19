import cv2
import time
class FaceDetect:
    def __init__(self):
        modelPath = "model/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(modelPath)

    def detect(self,image,biaoji=True):
        # Read the image
        # image = cv2.imread(imagePath)
        # st=time.time()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        self.faces = self.faceCascade.detectMultiScale(gray, 
        scaleFactor=1.1, 
        minNeighbors=5,    
        minSize=(30, 30),   
        flags = cv2.CASCADE_SCALE_IMAGE
        )
        # print ("Found {0} faces!".format(len(self.faces)))
        # Draw a rectangle around the faces
        if biaoji==True:
            for (x, y, w, h) in self.faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # cv2.imshow("Faces found" ,image)
        # count=1.0/(time.time()-st)
        # print("fps: {0}".format(count))
        return self.faces

    def realDetect(self):
        self.cap = cv2.VideoCapture(0)
        count =0
        while True:
            ret, img = self.cap.read()
            st=time.time()
            self.detect(img)
            cv2.waitKey(10)
            count=1.0/(time.time()-st)
            print("fps: {0}".format(count))

if __name__ == "__main__":
    face = FaceDetect()
    face.realDetect()