import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

from htmlformap import htmlformap

class mapwindow(QMainWindow):
    """docstring for MainWindow"""

    def __init__(self, org:str, dst:str):

        super(mapwindow, self).__init__()
        self.setWindowIcon(QIcon("image/nctu.jpeg"))
        self.setGeometry(560, 230, 800, 620)
        self.setWindowTitle("Routing Result")

        filepath = "route/" + org + "_" + dst + ".html"
        # print(filepath)

        main_frame = QWidget()
        layout = QHBoxLayout()

        self.backbutton = QPushButton("back")
        self.browser = QWebEngineView()

        current_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(current_dir, filepath)
        url = QUrl.fromLocalFile(filename)
        self.browser.setUrl(url)

        layout.addWidget(self.backbutton)
        layout.addWidget(self.browser)
        main_frame.setLayout(layout)

        self.setCentralWidget(main_frame)


if __name__ == "__main__":
    org = "northdoor"
    dst = "dorm3"

    # htmlformap(org, dst)
    app = QApplication(sys.argv)
    window = mapwindow(org, dst)
    window.show()
    sys.exit(app.exec_())