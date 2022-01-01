import threading
import sys
from posenet import posenet


from manager import Manager
#from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget

sim = threading.Thread(target = posenet)





## main program
app = QApplication(sys.argv)
manager = Manager()


# sim.start()

sys.exit(app.exec_())

# sim.join()