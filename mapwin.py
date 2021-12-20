import sys


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox)




class mapwin(QWidget):
    def __init__(self):  # Constructor
        super().__init__()
        self.back = False
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(250, 50, 800, 620)
        self.setWindowTitle('NCTU MAP')
        self.setWindowIcon(QIcon("image/nctu.jpeg"))
        self.setupUI()
        # self.show()

    def setupUI(self):


        self.title = QLabel("Sorry", self)
        self.title.move(350, 150)
        self.title.setStyleSheet("font-size: 30pt")


        # self.back_button.resize(20, 20) 
        self.back_button = QPushButton("Back", self)
        self.back_button.move(20, 20)
        self.back_button.setStyleSheet("background-color:gray")

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
    # app.setStyleSheet(stylesheet)
    window = mapwin()
    window.show()
    sys.exit(app.exec_())