import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QSlider, QLineEdit, QPushButton, QScrollArea,QHBoxLayout, QVBoxLayout, QMainWindow
# import Opencv module
import cv2
import numpy as np
import time
import threading
class App(QWidget):
    #this function initializes the window dimensions and title 
    def __init__(self):
        super().__init__()
        self.title = 'Frames'
        self.left = 270
        self.top = 20
        self.width = 740
        self.height = 300
        self.initUI()

    #this function sets the window shape, date and time, buttons and label dimensions(where the images are displayed) it only initialize the label, no image is set here 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(1100, 700)
        self.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self)
        self.dateTimeEdit.setEnabled(False)
        self.dateTimeEdit.setGeometry(QtCore.QRect(890, 10, 140, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setStyleSheet("background-color: rgb(53, 53, 53);\n"
"color: rgb(255, 255, 255);")
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 5, 5), QtCore.QTime(18, 30, 48)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(1050, 10, 35, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.refresh)
        self.pushButton2 = QtWidgets.QPushButton(self)
        self.pushButton2.setGeometry(QtCore.QRect(740, 150, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("done.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton2.setIcon(icon)
        self.pushButton2.setIconSize(QtCore.QSize(25,25))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        labeltext8= QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        labeltext8.setFont(font)
        labeltext8.setText("ID:")
        m=30
        n=20
        labeltext8.setGeometry(QtCore.QRect(420,100, 25, 30))
        self.labeltext7= QtWidgets.QLabel(self)
        self.labeltext7.setFont(font)
        self.labeltext7.setGeometry(QtCore.QRect(450, 100, 20, 30))
        labeltext9= QtWidgets.QLabel(self)
        labeltext9.setFont(font)
        labeltext9.setText("Jet:")
        labeltext9.setGeometry(QtCore.QRect(500,100, 50, 30))
        self.labeltext6= QtWidgets.QLabel(self)
        self.labeltext6.setFont(font)
        self.labeltext6.setGeometry(QtCore.QRect(530,100, 20, 30))
        labeltext2= QtWidgets.QLabel(self)
        labeltext2.setFont(font)
        labeltext2.setText("Time:")
        labeltext2.setGeometry(QtCore.QRect(570,100, 45, 30))
        self.labeltext3= QtWidgets.QLabel(self)
        self.labeltext3.setFont(font)
        self.labeltext3.setGeometry(QtCore.QRect(615,100, 70, 30))
       
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(280, 180, 500, 331))

        self.toolButton = QtWidgets.QToolButton(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("change.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(25, 25))
        self.toolButton.setGeometry(QtCore.QRect(280,150, 41, 31))
        self.toolButton.setObjectName("toolButton")

        self.show()
        self.img()

    #the frames are retrevied in this function
    def img(self):
        cap = cv2.imread('C:/Users/owner/Desktop/Thesis/3712-left.jpg')
        cap2 = cv2.imread('C:/Users/owner/Desktop/Thesis/3711-right.jpg')
        cap3 = cv2.imread('C:/Users/owner/Desktop/Thesis/3711-left.jpg')
        cap4 = cv2.imread('C:/Users/owner/Desktop/Thesis/3710-right.jpg')
        cap5 = cv2.imread('C:/Users/owner/Desktop/Thesis/3710-left.jpg')
        #create an array of images having the [frame, frameID,JetsonID,timestamp,Flag "1 is an accident"]
        images=[[cap,34,2,"10:00:07",1],[cap2,33,1,"10:00:06",1],[cap3,32,1,"10:00:05",1],[cap4,31,2,"10:00:03",1],[cap5,30,2,"10:00:02",1]]
        print("Received Frames")
        count=len(images);
        self.delay(images,count)
        self.toolButton.clicked.connect(lambda: self.printd(images))

    def button(self,images,count):
        #check if there are still more frames to be displayed
        if (count>0):
            self.pushButton2.clicked.connect(lambda: self.delay(images,count))
        #all the frames are shown so no more frames to be displayed
        else:
            print("No New Frames")

        #this function convert the cv image to QTlabel to be displayed
    def delay(self,images,x):
        rgbImage = cv2.cvtColor(images[x-1][0], cv2.COLOR_BGR2RGB)
        convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                             QtGui.QImage.Format_RGB888)
        convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
        pixmap = QPixmap(convertToQtFormat)
        resizeImage = pixmap.scaled(540, 580, QtCore.Qt.KeepAspectRatio)
        #display the image as QT image
        self.label.setPixmap(resizeImage)
        self.label.setStyleSheet("border: 5px solid red")
        #display the Jetson ID
        self.labeltext6.setText(str(images[x-1][2]))
        #display the Timestamp
        self.labeltext3.setText(str(images[x-1][3]))
        #display the FrameID
        self.labeltext7.setText(str(images[x-1][1]))
        self.button(images,x-1)

        #this function prints the confirmation messagebox that appears after the user click on the change icon
    def printd(self,images):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Would you like to change the label of this image?")
        msgBox.setWindowTitle("Confirmation Message")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            #change the label color to green 
            self.label.setStyleSheet("border: 5px solid green")
        print("Updated Frames are sent")

    def refresh(self):
        self.__init__()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())