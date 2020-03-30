from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl, QTimer
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure
import numpy as np
#import matplotlib.pyplot as plt
#import requests
#import pandas as pd
#from  more_itertools import unique_everseen
#from random import shuffle as sf
import cv2
import time
import socket
import base64
import requests as req


class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('player.png'))
 
        #p =self.palette()
        #p.setColor(QPalette.Window, Qt.black)
        #self.setPalette(p)
        
        
        #self.clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #self.clientsocket.connect(('192.168.0.47',2000))
        
        
        milli_sec = int(round(time.time() * 1000))
        print(milli_sec)
        
        self.timer = QTimer()
         
        self.timer.timeout.connect(self.viewCam)
        
        fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        self.out = cv2.VideoWriter('C:/Users/brahm/OneDrive/Desktop/webcam/'+str(milli_sec)+'.mp4', fourcc, 30.0, (640, 480))
 
        self.init_ui()
 
 
        self.show()
 
 
    def init_ui(self):
 
        #create media player object
        #canvas = Bar(self, width=9, height=4)
        #canvas.move(0, 0)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
 
 
        #create videowidget object
 
        videowidget = QVideoWidget()
 
        #self.mediaPlayer.setVideoOutput(videowidget)
 
        #create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)
 
 
        self.videobutton = QPushButton('start')
        self.videobutton.clicked.connect(self.record)
    
 
        #create button for playing
        self.playBtn = QPushButton()
        #self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)
 
 
 
        #create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
 
 
 
        #create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
 
 
        #create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)
 
        #set widgets to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.videobutton)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)
 
 
 
        #create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)
 
 
        self.setLayout(vboxLayout)
 
        self.mediaPlayer.setVideoOutput(videowidget)
 
 
        #media player signals
 
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.error.connect(self.handle_errors) 
        self.label.setText("Ready")
        
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/brahm/OneDrive/Desktop/face exp node/రాష్ట్రపతి పాలన ఎప్పుడు, ఎందుకు విధిస్తారు_ ఆర్టికల్ 356 ఏం చెబుతోంది_ - BBC New.wmv")))
 
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
 
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            print(filename,"file") 
 
    def play_video(self):
        
        
        
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            print(self.mediaPlayer.state(),"00000")
 
        else:
            self.mediaPlayer.play()
            print('mediaStatus: ' + str(self.mediaPlayer.mediaStatus()))
            print(self.mediaPlayer.state(),"2222")
            print(QMediaPlayer.PlayingState,"3333")
 
    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)
 
            )
 
        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
 
            )
 
    def position_changed(self, position):
        self.slider.setValue(position)
 
 
    def duration_changed(self, duration):
        self.slider.setRange(0, duration)
 
 
    def set_position(self, position):
        self.mediaPlayer.setPosition(position)
 
 
    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())
        print(self.mediaPlayer.error, 'error')
        print('mediaStatus: ' + str(self.mediaPlayer.mediaStatus()))
        print('error: ' + str(self.mediaPlayer.error()))
      
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        
        
        encoded, buffer = cv2.imencode('.jpg', image)
        
        jpg_as_text = base64.b64encode(buffer)
        
        
        print("jpg_as_text", jpg_as_text)
        
        #print("buffer", buffer)
        
        #data = {'name': image}
        
        #resp = req.post("https://httpbin.org/post", data)
        #print(resp.text)
        
        
        
        
        #data = pickle.dumps(image)
        
        
        #print("data", data)
        
        #self.clientsocket.sendall(struct.pack("H", len(data))+data)
        
        
        
        self.out.write(image) 
        # convert image to RGB format
            
    def record(self):
        if not self.timer.isActive():
           self.cap = cv2.VideoCapture(0)
           self.timer.start()
           self.videobutton.setText("Stop")
        else:
            self.timer.stop()
            self.cap.release()
            print("data", self.out)
            self.out.release()
            
            
            
            
            # update control_bt text
            self.videobutton.setText("Start")

 
 
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())