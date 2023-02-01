# base file to start the application.

import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("groundzero ui")
        
        self.statusBar() # call this once to make it appear.
        self.statusBar().showMessage("Welcome to GroundZero")


        self.viewMenu = self.menuBar().addMenu("View")

        # set up dock widgets (properties viewer, shell, graphs, node toolbox)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec()
