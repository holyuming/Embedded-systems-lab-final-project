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
        # self.mapwindow = mapwindow("", "")
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
        self.tourw.dorm8.clicked.connect(self.opendorm8)
        self.tourw.dorm9.clicked.connect(self.opendorm9)
        self.tourw.dorm10.clicked.connect(self.opendorm10)
        self.tourw.dorm11.clicked.connect(self.opendorm11)
        self.tourw.dorm12.clicked.connect(self.opendorm12)
        self.tourw.dorm13.clicked.connect(self.opendorm13)
        self.tourw.dorm3.clicked.connect(self.opendorm3)
        self.tourw.dormg2.clicked.connect(self.opendormg2)


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

    def opendorm8(self):
        self.dorm = dormwin("dorm8")
        self.dorm.show()
    
    def opendorm9(self):
        self.dorm = dormwin("dorm9")
        self.dorm.show()

    def opendorm10(self):
        self.dorm = dormwin("dorm10")
        self.dorm.show()

    def opendorm11(self):
        self.dorm = dormwin("dorm11")
        self.dorm.show()
    
    def opendorm12(self):
        self.dorm = dormwin("dorm12")
        self.dorm.show()

    def opendorm13(self):
        self.dorm = dormwin("dorm13")
        self.dorm.show()

    def opendorm3(self):
        self.dorm = dormwin("dorm3")
        self.dorm.show()
    
    def opendormg2(self):
        self.dorm = dormwin("dormg2")
        self.dorm.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())