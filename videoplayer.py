import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2
import time
from ffpyplayer.player import MediaPlayer

from video import *

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_video()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam) 
        self.timer.timeout.connect(self.viewvideo)
        # set control_bt callback clicked  function
        self.ui.start.clicked.connect(self.controlTimer)
        self.ui.stop.clicked.connect(self.stop)
        
        
        milli_sec = int(round(time.time() * 1000))
        print(milli_sec)
        
        
        fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        self.out = cv2.VideoWriter('C:/Users/brahm/OneDrive/Desktop/webcam/'+str(milli_sec)+'.mp4', fourcc, 30.0, (640, 480))

    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        
        self.out.write(image) 
        # convert image to RGB format
        
        
        
    def viewvideo(self):
        # read image in BGR format
        ret, image = self.video.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        
            # create video capture
            self.cap = cv2.VideoCapture(0)
            
            fps = self.cap.get(cv2.CAP_PROP_FPS)
            
            print("fps", fps)
            
            self.video = cv2.VideoCapture("C:/Users/brahm/OneDrive/Desktop/రాష్ట్రపతి పాలన ఎప్పుడు, ఎందుకు విధిస్తారు_ ఆర్టికల్ 356 ఏం చెబుతోంది_ - BBC New.mp4")
           
            self.video.set(cv2.CAP_PROP_FPS, 30)
            
            fpsdata = self.cap.get(cv2.CAP_PROP_FPS)
            
            print("fpsdata", fpsdata)
            
            self.player = MediaPlayer("C:/Users/brahm/OneDrive/Desktop/రాష్ట్రపతి పాలన ఎప్పుడు, ఎందుకు విధిస్తారు_ ఆర్టికల్ 356 ఏం చెబుతోంది_ - BBC New.mp4")
            
            # start timer
            self.timer.start()
            # update control_bt text
            #self.ui.start.setText("Stop")
        # if timer is started
        
            
            
            
    def stop(self):        
             
            self.timer.stop()
            # release video capture
            self.cap.release()
            self.out.release()
            # update control_bt text
           # self.ui.start.setText("Start")
            
            
            


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())