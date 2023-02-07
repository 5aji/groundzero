# base file to start the application.

import sys

from qtpy.QtCore import QObject
from qtpy.QtWidgets import QMainWindow, QApplication, QToolBar

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.manager import QtKernelManager


class pyJupyterWidget(RichJupyterWidget):
    def __init__(self):
        super().__init__()
        kernel_manager = QtKernelManager(kernel_name='python3')
        kernel_manager.start_kernel()

        kernel_client = kernel_manager.client()
        kernel_client.start_channels()

        self.kernel_manager = kernel_manager
        self.kernel_client = kernel_client


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("groundzero ui")

        self.statusBar()  # call this once to make it appear.
        self.statusBar().showMessage("Welcome to GroundZero")

        self.viewMenu = self.menuBar().addMenu("View")

        # set up dock widgets (properties viewer, shell, graphs, node toolbox)
        self.console_widget = pyJupyterWidget()
        self.setCentralWidget(self.console_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec()
