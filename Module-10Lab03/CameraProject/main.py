"""My Camera Application


    author: Bakibillah
 """

 
import sys
from turtle import window_width
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QTimer
import cv2


# create a windows class
class Window(QWidget):
    """ Main app Window """
    def __init__(self):
        super().__init__()

        #  var for app window
        self.window_width = 640
        self.window_height = 400

        # image variable
        self.img_width = 640
        self.img_height = 400

        # setup the window
        self.setWindowTitle("My Camera App")
        self.setGeometry(100,100,self.window_width,self.window_height)
        self.setFixedSize(self.window_width,self.window_height)

        # setup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.ui()


    def ui(self):
        """ Contains all ui things """
        # image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0,0, self.img_width, self.img_height)

        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        self.show()

    def update(self):
        """ Update Frame """
        _,self.frame = self.cap.read()

        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB) # open cv always B GB read kore amdr drkre RGB
        height,width,channel = frame.shape
        step = channel*width

        q_frame = QImage(frame.data, width, height, step,QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_frame))

    def save_img(self):
        """ Save image from camera """
        pass

    def record(self):
        """ record Video """
        pass

#  run
app  = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())