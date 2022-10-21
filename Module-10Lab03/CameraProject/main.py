"""My Camera Application


    author: Bakibillah
 """

 
import sys
from turtle import window_width
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
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

        self.ui()


    def ui(self):
        """ Contains all ui things """
        # image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0,0, self.img_width, self.img_height)
        self.show()

    def update(self):
        """ Update Frame """
        pass

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