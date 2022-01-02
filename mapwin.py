import sys


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox, QComboBox)




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
        
        layout = QVBoxLayout()

        # self.back_button.resize(20, 20) 
        self.back_button = QPushButton("Back", self)
        self.back_button.move(20, 20)
        self.back_button.setStyleSheet("background-color:gray ; font-size : 30pt")

        # org label
        self.orglabel = QLabel("FROM:")
        self.orglabel.setStyleSheet("font-size : 40pt")


        # org combobox
        self.org = QComboBox(self)
        self.org.setStyleSheet("font-size : 30pt")
        self.org.addItems(["northdoor", "southdoor"])

        # dst label
        self.dstlabel = QLabel("DESTINATION")
        self.dstlabel.setStyleSheet("font-size : 40pt")

        # dst combobox
        self.dst = QComboBox(self)
        self.dst.setStyleSheet("font-size : 30pt")
        self.dst.addItems(["dorm7", "dorm8", "dorm9", "dorm10", "dorm12", "dorm13", "dormg2"])

        # enter button
        self.enterbutton = QPushButton("ENTER")
        self.enterbutton.setStyleSheet("font-size : 50pt")
        

        layout.addWidget(self.back_button)
        layout.addStretch(1)
        layout.addWidget(self.orglabel)
        layout.addWidget(self.org)
        layout.addStretch(1)
        layout.addWidget(self.dstlabel)
        layout.addWidget(self.dst)
        layout.addStretch(1)
        layout.addWidget(self.enterbutton)

        self.setLayout(layout)
    

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet(stylesheet)
    window = mapwin()
    window.show()
    sys.exit(app.exec_())