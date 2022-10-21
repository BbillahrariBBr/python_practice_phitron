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

        # load icon
        self.camera_icon = QIcon(cap_icon_path)

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
        # layout 
        grid = QGridLayout()
        self.setLayout(grid)

        # image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0,0, self.img_width, self.img_height)

        # capture button
        self.capture_btn = QPushButton(self)
        self.capture_btn.setIcon(self.camera_icon)
        self.capture_btn.setStyleSheet("border-radius: 30; border: 2px solid black; border-width: 3px")
        self.capture_btn.setFixedSize(60,60)
        self.capture_btn.clicked.connect(self.save_img)

        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        # add things to the layout
        grid.addWidget(self.capture_btn,0,0)
        grid.addWidget(self.image_label,0,1)

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
        print("Saving Image")
        cv2.imwrite("my_img.jpg", self.frame)

    def record(self):
        """ record Video """
        pass

#  run
cap_icon_path = 'assets/capture.png'
app  = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())