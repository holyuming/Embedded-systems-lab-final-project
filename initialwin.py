import sys


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox)



stylesheet = """
    QWidget {
        background-color: gray;
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
        self.setGeometry(250, 50, 1920, 1080)
        self.setWindowTitle('NCTU FOOD GUIDE SYSTEM')
        self.setWindowIcon(QIcon("image/nctu.jpeg"))
        self.setStyleSheet(stylesheet)                                      # <========
        self.setupUI()
        # self.show()

    def setupUI(self):

        
        self.title = QLabel("NCTU FOOD GUIDE SYSTEM")
        self.title.setFont(QFont('Arial', 100))
        self.title.setStyleSheet("font: bold")
        self.title.setAlignment(Qt.AlignCenter)

        self.enter_button = QPushButton("Enter")
        self.enter_button.resize(300, 500) 
        self.enter_button.clicked.connect(self.enter1)

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
        self.mapbox = QCheckBox("map")
        self.mapbox.setFont(QFont('Arial', 50))
        self.tourbox = QCheckBox("tour")
        self.tourbox.setFont(QFont('Arial', 50))
        self.mapbox.setStyleSheet("QCheckBox::indicator { width: 80px; height: 80px;}")
        self.tourbox.setStyleSheet("QCheckBox::indicator { width: 80px; height: 80px;}")
            

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
        self.wholewindow .addWidget(self.enter_button)
        self.wholewindow.addStretch(1)

        # Set main layout of the window
        self.setLayout(self.wholewindow)

    def enter1(self):
        self.func1 = self.func2 = False
        if self.mapbox.isChecked():
            self.func1 = True
        if self.tourbox.isChecked():
            self.func2 = True
        # print("Mapbox checked: ", self.func1)
        # print("Tourbox checked:", self.func2)

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