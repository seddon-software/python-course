import os, time, numpy as np

import cothread
from cothread.catools import *

from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

# Enable Qt processing, hang onto application instance if needed.
qtapp = cothread.iqt()      # Not needed if not using Qt


def f():
    for n in np.arange(0.1, 1.0, 0.01):
    caput("chris:amplitude", n)
    print(f'{caget("chris:amplitude"):0.2f}')
    time.sleep(0.25)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    # Finally allow all background tasks to run to completion.
    cothread.WaitForQuit()      # Or some other blocking construct
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    