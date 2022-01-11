import sys


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox)


# general stylesheet                                                # <========
stylesheet = """


"""


class tourwin(QWidget):
    def __init__(self):  # Constructor
        super().__init__()

        # Dorm location  [width, height]                                              needs to be done, tedious work
        self.dorm = {
            "dorm7"   : [900, 560],
            "dorm8"   : [900, 640],
            "dorm9"   : [600, 220],
            "dorm10"  : [600, 140],
            "dorm11"  : [710, 140],
            "dorm12"  : [550, 720],
            "dorm13"  : [600, 800],
            "dorm3"   : [650, 880],
            "dormg2"  : [800, 720],
        }
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(210, 50, 1500, 1000)
        self.setFixedSize(1500, 1000)
        self.setWindowTitle('NCTU MAP')
        self.setWindowIcon(QIcon("image/nctu.jpeg"))
        self.setStyleSheet(stylesheet)                                      # <========
        self.setupUI()


    def setupUI(self):


        # Create NCTU map
        self.nctumap = "image/nctumap/nctumap.jpg"
        self.map = QLabel(self)
        try:
            with open(self.nctumap):
                pixmap = QPixmap(self.nctumap)
                pixmap = pixmap.scaled(1500, 1000, Qt.KeepAspectRatio)
                self.map.setPixmap(pixmap)
                # self.map.resize(800, 620)
        except FileNotFoundError:
            print("Image not found.", self.nctumap)


        # Back button 
        self.back_button = QPushButton("Back", self)
        self.back_button.move(20, 20)
        # Back button stylesheet                                                                   <========
        self.back_button.setStyleSheet("background-color : gray ; font-size : 30pt ; font : bold")


        # self.back_button.clicked.connect(self.test)


        # Dorm 7
        self.dorm7 = QPushButton("七舍", self)
        self.dorm7.move(self.dorm["dorm7"][0], self.dorm["dorm7"][1])
        self.dorm7.setStyleSheet("background-color : yellow ; font-size : 35pt")

        # Dorm 8
        self.dorm8 = QPushButton("八舍", self)
        self.dorm8.move(self.dorm["dorm8"][0], self.dorm["dorm8"][1])
        self.dorm8.setStyleSheet("background-color : yellow ; font-size : 35pt")

        # Dorm 9
        self.dorm9 = QPushButton("九舍", self)
        self.dorm9.move(self.dorm["dorm9"][0], self.dorm["dorm9"][1])
        self.dorm9.setStyleSheet("background-color : yellow ; font-size : 35pt")

        # Dorm 10
        self.dorm10 = QPushButton("十舍", self)
        self.dorm10.move(self.dorm["dorm10"][0], self.dorm["dorm10"][1])
        self.dorm10.setStyleSheet("background-color : yellow ; font-size : 35pt")

        # Dorm 11
        self.dorm11 = QPushButton("十一舍", self)
        self.dorm11.move(self.dorm["dorm11"][0], self.dorm["dorm11"][1])
        self.dorm11.setStyleSheet("background-color : yellow ; font-size : 35pt")

        # Dorm 12
        self.dorm12 = QPushButton("十二舍", self)
        self.dorm12.move(self.dorm["dorm12"][0], self.dorm["dorm12"][1])
        self.dorm12.setStyleSheet("background-color : yellow ; font-size : 35pt")

        # Dorm 13
        self.dorm13 = QPushButton("十三舍", self)
        self.dorm13.move(self.dorm["dorm13"][0], self.dorm["dorm13"][1])
        self.dorm13.setStyleSheet("background-color : yellow ; font-size : 35pt")

        # Dorm 3
        self.dorm3 = QPushButton("研三舍", self)
        self.dorm3.move(self.dorm["dorm3"][0], self.dorm["dorm3"][1])
        self.dorm3.setStyleSheet("background-color : yellow ; font-size : 35pt")

        # Dorm g2
        self.dormg2 = QPushButton("女二舍", self)
        self.dormg2.move(self.dorm["dormg2"][0], self.dorm["dormg2"][1])
        self.dormg2.setStyleSheet("background-color : yellow ; font-size : 35pt")

        



        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = tourwin()
    window.show()
    sys.exit(app.exec_())