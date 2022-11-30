# base file to start the application.

from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("groundzero ui")
        
        self.statusBar() # call this once to make it go.
        self.statusBar().showMessage("hllow")

        # set up dock widgets (properties viewer, shell, graphs, node toolbox)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec()
