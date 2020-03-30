
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import cv2


class Video(object):
    def __init__(self,path):
        self.path = path
        #self.videobutton = QPushButton('start')
        #self.cap = cv2.VideoCapture(0)
        #ret, image = self.cap.read()
        
        #print("ret", ret)
        
        #print("image", image)
        
             
                 
        
    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"

movie = Movie_MP4("C:/Users/brahm/OneDrive/Desktop/రాష్ట్రపతి పాలన ఎప్పుడు, ఎందుకు విధిస్తారు_ ఆర్టికల్ 356 ఏం చెబుతోంది_ - BBC New.mp4")
#if input("Press enter to play, anything else to exit") == '' :
movie.play()
  