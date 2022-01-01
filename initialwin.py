import sys


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox)



stylesheet = """
    QWidget {
        background-color: black;
        background-position: center;
    }
    QPushButton {
        background-repeat: no-repeat; 
        background-position: center;
        background-color: white;
        font: bold;
        font-size: 30pt;
    }
    QCheckBox {
        background-repeat: no-repeat; 
        background-position: center;
        background-color: yellow;
    }
    QVBoxLayout{
        background-repeat: no-repeat; 
        background-position: center;
        background-color: purple;
    }    
"""

test = """ background-image: url("image/nctu.jpeg"); """




class Window(QWidget):
    def __init__(self):  # Constructor
        super().__init__()
        self.func1 = False
        self.func2 = False
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(560, 230, 800, 620)
        self.setWindowTitle('NCTU FOOD GUIDE SYSTEM')
        self.setWindowIcon(QIcon("image/nctu.jpeg"))
        self.setStyleSheet(stylesheet)                                      # <========
        self.setupUI()
        # self.show()

    def setupUI(self):

        
        self.title = QLabel("NCTU FOOD GUIDE \n SYSTEM")
        self.title.setFont(QFont('ubuntu', 90))
        self.title.setStyleSheet("font: bold ; color:white")
        self.title.setAlignment(Qt.AlignCenter)

        # Create NCTU logo 
        self.nctuimage = "image/nctu.jpeg"
        self.logo = QLabel(self)
        try:
            with open(self.nctuimage):
                pixmap = QPixmap(self.nctuimage)
                self.logo.setPixmap(pixmap)
                self.logo.setAlignment(Qt.AlignHCenter)
                self.logo.resize(20, 20)
        except FileNotFoundError:
            print("Image not found.")

        # Create checkboxes and line edit widgets
        functionoption = QHBoxLayout()
        self.mapbox = QPushButton("map")
        self.mapbox.setStyleSheet("font-size:60pt ; background-color : blue")
        self.tourbox = QPushButton(" tour")
        self.tourbox.setStyleSheet("font-size:60pt; background-color : blue")
            

        functionoption.addWidget(self.mapbox)
        functionoption.addWidget(self.tourbox)

        # Add other layouts to main layout
        self.wholewindow = QVBoxLayout()
        self.wholewindow .addWidget(self.title)
        self.wholewindow.addStretch(1)
        self.wholewindow .addWidget(self.logo)
        self.wholewindow.addStretch(1)
        self.wholewindow.addLayout(functionoption)
        self.wholewindow.addStretch(1)

        # Set main layout of the window
        self.setLayout(self.wholewindow)

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
    app.setStyleSheet(stylesheet)
    window = Window()
    window.show()
    sys.exit(app.exec_())