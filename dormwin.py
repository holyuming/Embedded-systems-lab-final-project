import sys
import os


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox)


# general stylesheet                                                # <========
stylesheet = """


"""


class dormwin(QWidget):
    def __init__(self, dormname : str):  # Constructor
        super().__init__()

        self.dormname = dormname

        # Dorm location  [width, height]                                              needs to be done, tedious work
        self.dorm = {
            "dorm7"   : [550, 370],
            "dorm8"   : [],
            "dorm9"   : [],
            "dorm10"  : [],
            "dorm11"  : [],
            "dorm12"  : [],
            "dorm3"   : [],
            "dormg2"  : [],
        }
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setStyleSheet("background-color : gray")
        self.setGeometry(560, 250, 800, 620)
        self.setWindowTitle(self.dormname)
        self.setWindowIcon(QIcon("image/nctu.jpeg"))
        # self.setStyleSheet(stylesheet)                                      # <========
        self.setupUI()


    def setupUI(self):

        wholewindow = QHBoxLayout(self)


        # Create list of file
        self.index = 0
        self.picnumber = len(os.listdir("image/" + self.dormname ))
        self.picdir = "image/" + self.dormname 
        self.picpath = self.picdir + "/" + str(self.index) + ".jpg"

        self.dormimg = QLabel(self)
        self.openpic()



        # Previous button 
        self.previous = QPushButton("<<", self)
        self.previous.setFixedSize(170, 80)
        # self.previous.move(20, 300)
        self.previous.setStyleSheet("background-color : gray ; font-size : 50pt ; font : bold")
        self.previous.clicked.connect(self.previouspic)


        # Next button
        self.next = QPushButton(">>", self)
        self.next.setFixedSize(170, 80)
        # self.next.move(700, 300)
        self.next.setStyleSheet("background-color : gray ; font-size : 50pt ; font : bold")
        self.next.clicked.connect(self.nextpic)


        # Set layout
        wholewindow.addWidget(self.previous)
        wholewindow.addWidget(self.dormimg, alignment=Qt.AlignCenter)
        wholewindow.addWidget(self.next)

        self.setLayout(wholewindow)
    
    def nextpic(self):
        if (self.index < self.picnumber - 1):
            self.index += 1
            self.openpic()
        else:
            errormsg = QMessageBox()
            errormsg.warning(self, "Error Message", "This is the last picture", QMessageBox.Close)            
        

    def previouspic(self):
        if (self.index != 0):
            self.index -= 1
            self.openpic()
        else:
            errormsg = QMessageBox()
            errormsg.warning(self, "Error Message", "This is the first picture", QMessageBox.Close)

    def openpic(self):
        self.picpath = self.picdir + "/" + str(self.index) + ".jpg"
        try:
            with open(self.picpath):
                pixmap = QPixmap(self.picpath)
                pixmap = pixmap.scaled(600, 600, Qt.KeepAspectRatio)
                print(pixmap.size())
                self.dormimg.setPixmap(pixmap)
                # self.dormimg.resize(800, 620)
        except FileNotFoundError:
            print("Image not found.", self.picpath)



    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = dormwin("dorm3")
    window.show()
    sys.exit(app.exec_())