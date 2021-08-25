import os, time, numpy as np
from epics import PV

import cothread
from cothread.catools import *

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

# Enable Qt processing, hang onto application instance if needed.
qtapp = cothread.iqt()      # Not needed if not using Qt

def on_button_clicked():
    def update(pv, textbox):
        value = textbox.text()
        try:
            if not value == "":
                caput(pv, float(value))
        except:
            print(f"Invalid value for {pv}:{value}")
    update("chris:freqCalc", on_button_clicked.frequencyTextbox)
    update("chris:offset", on_button_clicked.offsetTextbox)
    update("chris:amplitude", on_button_clicked.amplitudeTextbox)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        pv1 = PV("chris:freqCalc")
        pv1.put(2)
#        caput("chris:freqCalc", 2.0)

        self.amplitude = 0.1
        self.delta = 0.01
        graphWidget = pg.PlotWidget()

        frequencyTextbox = QLineEdit()
        frequencyLabel = QLabel()
        frequencyLabel.setText('Frequency:')
        offsetTextbox = QLineEdit()
        offsetLabel = QLabel()
        offsetLabel.setText('Offset:')
        amplitudeTextbox = QLineEdit()
        amplitudeLabel = QLabel()
        amplitudeLabel.setText('Amplitude:')

        button = QPushButton('update')
        button.clicked.connect(on_button_clicked)
        on_button_clicked.frequencyTextbox = frequencyTextbox
        on_button_clicked.offsetTextbox = offsetTextbox
        on_button_clicked.amplitudeTextbox = amplitudeTextbox

        layout = QVBoxLayout()
        layout.addWidget(graphWidget)
        layout2 = QHBoxLayout()
        layout2.addWidget(frequencyLabel)
        layout2.addWidget(frequencyTextbox)
        layout2.addWidget(offsetLabel)
        layout2.addWidget(offsetTextbox)
        layout2.addWidget(amplitudeLabel)
        layout2.addWidget(amplitudeTextbox)
        layout2.addWidget(button)
        canvas = QWidget()
        self.setCentralWidget(canvas)
        canvas.setLayout(layout)
        panel = QWidget()
        layout.addWidget(panel)
        panel.setLayout(layout2)
        #self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))  # 100 time points
        self.y = [0.0]*100

        graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  graphWidget.plot(self.x, self.y, pen=pen)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        if self.amplitude > 0.8: self.delta = -0.01
        if self.amplitude < 0.1: self.delta = +0.01
        self.amplitude += self.delta
        caput("chris:amplitude", self.amplitude)

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        self.y = self.y[1:]  # Remove the first
        self.y.append(caget("chris:function"))
        self.data_line.setData(self.x, self.y)  # Update the data.

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    # Finally allow all background tasks to run to completion.
    cothread.WaitForQuit()      # Or some other blocking construct
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    