from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import os, sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl, QTimer
import cv2
import time
#import socket
#import pickle
import json
#import requests as req
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('player.png'))
        
        
        #reqdata = req.get('http://192.168.0.47:2000/getcsvfile/strenght-weakness_bp')
        #data = reqdata.json()
        
        #print("data", data)
        
        #192.168.0.47
        #http://192.168.0.47:2000/getvideo/strenght-weakness_bp
 
        #p =self.palette()
        #p.setColor(QPalette.Window, Qt.black)
        #self.setPalette(p)
        
        #data = {'name': 'Peter'}

        #resp = req.post("https://httpbin.org/post", data)
        #print(resp.text)
        
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
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
 
 
        #create videowidget object
 
        videowidget = QVideoWidget()
 
 
        #create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)
        
        self.videobutton = QPushButton('start')
        self.videobutton.clicked.connect(self.record)
 
 
 
        #create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
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
 
    def open_file(self):
        #sender = self.sender()
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
 
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
 
 
    def play_video(self):
        
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
 
        else:
            self.mediaPlayer.play()
            
            print('mediaStatus: ' + str(self.mediaPlayer.mediaStatus()))
 
 
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
        print("position", position)
        self.mediaPlayer.setPosition(position)
 
 
    def handle_errors(self):
        print(self.mediaPlayer.error, 'error')
        print('error: ' + str(self.mediaPlayer.error()))
        print('mediaStatus: ' + str(self.mediaPlayer.mediaStatus()))
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())
 
 
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        
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
 