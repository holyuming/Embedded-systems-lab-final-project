import sys
import threading

from initialwin import Window
from mapwindow import mapwindow
from tourwin import tourwin
from mapwin import mapwin
from dormwin import dormwin


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget



class Manager(threading.Thread):
    def __init__(self) -> None:
        self.initwin = Window()
        self.tourw = tourwin()
        self.mapw = mapwin()
        self.mapwindow = mapwindow("", "")
        self.initwin.show()

        # Set the default of tourbox to true
        self.initwin.tourbox.setChecked(True)

        # two functions
        self.initwin.mapbox.clicked.connect(self.maphit)
        self.initwin.tourbox.clicked.connect(self.tourhit)


        # If the back button of tourwindow being hit
        self.tourw.back_button.clicked.connect(self.tourwbackhit)

        # If the enter button of mapw being hit
        self.mapw.enterbutton.clicked.connect(self.mapwenterhit)

        # If the back button of mapwindow being hit
        # self.mapwindow.backbutton.clicked.connect(self.mapwindowbackhit)

        # Dorm pic button being hit
        self.tourw.dorm7.clicked.connect(self.opendorm7)

        # If the back button of mapwindow being hit
        self.mapw.back_button.clicked.connect(self.mapwbackhit)
    
               
    def maphit(self):
        self.tourw.hide()
        self.mapw.show()

    def mapwbackhit(self):
        self.mapw.hide()
        self.initwin.show()

    def mapwenterhit(self):
        org = self.mapw.org.currentText()
        dst = self.mapw.dst.currentText()
        # print(org, dst)
        self.mapwindow = mapwindow(org, dst)
        self.mapwindow.show()
        

    def tourhit(self):
        self.tourw.hide()
        self.tourw.show()
        

    def tourwbackhit(self):
        self.tourw.hide()
        self.initwin.show()
    
    def opendorm7(self):
        self.dorm = dormwin("dorm7")
        self.dorm.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())