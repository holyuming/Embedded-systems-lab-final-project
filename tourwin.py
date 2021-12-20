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
        self.setGeometry(500, 250, 800, 620)
        self.setFixedSize(800, 620)
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
                self.map.setPixmap(pixmap)
                self.map.resize(800, 620)
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
        self.dorm7.setStyleSheet("background-color : yellow")

    # def test(self):
    #     print("back")
    #     self.map.hide()
    

    def closeEvent(self, event):
        """
        Display a QMessageBox when asking the user if they want to
        quit the program.
        """
        # set up message box
        answer = QMessageBox.question(self, "Quit Application?",
                                      "Are you sure you want to Quit?", QMessageBox.No | QMessageBox.Yes,
                                      QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            event.accept()  # accept the event and close the application
        else:
            event.ignore()  # ignore the close event
        

        



        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = tourwin()
    window.show()
    sys.exit(app.exec_())