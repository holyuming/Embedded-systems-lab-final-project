import sys

from initialwin import Window
from tourwin import tourwin
from mapwin import mapwin
from dormwin import dormwin


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget



class Manager():
    def __init__(self) -> None:
        self.initwin = Window()
        self.tourw = tourwin()
        self.mapw = mapwin()
        self.initwin.show()

        # Set the default of tourbox to true
        self.initwin.tourbox.setChecked(True)

        # Unchecked the other checkbox under some conditions
        self.initwin.mapbox.stateChanged.connect(self.unchecktour)
        self.initwin.tourbox.stateChanged.connect(self.uncheckmap)

        # If the enter button of initwindow being hit
        self.initwin.enter_button.clicked.connect(self.initenterhit)

        # If the back button of tourwindow being hit
        self.tourw.back_button.clicked.connect(self.tourwbackhit)

        # Dorm pic button being hit
        self.tourw.dorm7.clicked.connect(self.opendorm7)

        # If the back button of mapwindow being hit
        self.mapw.back_button.clicked.connect(self.mapwbackhit)

    def unchecktour(self, state): 
        if state == Qt.Checked:
            self.initwin.tourbox.setChecked(False)
        else:
            self.initwin.tourbox.setChecked(True)

    def uncheckmap(self, state):
        if state == Qt.Checked:
            self.initwin.mapbox.setChecked(False)
        else:
            self.initwin.mapbox.setChecked(True)
               
    def initenterhit(self):
        if (self.initwin.tourbox.isChecked()):
            self.tourw.show()
            self.initwin.hide()
        else:
            self.mapw.show()
            self.initwin.hide()

    def tourwbackhit(self):
        self.tourw.hide()
        self.initwin.show()

    def mapwbackhit(self):
        self.mapw.hide()
        self.initwin.show()
    
    def opendorm7(self):
        self.dorm7 = dormwin("dorm7")
        self.dorm7.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())