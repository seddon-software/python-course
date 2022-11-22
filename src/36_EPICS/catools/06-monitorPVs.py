'''
    Example showing how to monitor PVs
'''
import cothread
from cothread.catools import *
import os, time
from epics import PV
import sys  # We need sys so that we can pass argv to QApplication


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QLineEdit, QMessageBox

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

# callback for monitoring changes in PVs
def print_update(value, index):
    print(value.name, index, value)
    # note value is not quite a 'float', but + converts value to a float
    print(type(value), type(+value))


# Enable Qt processing, hang onto application instance if needed.
qtapp = cothread.iqt()      # Not needed if not using Qt

# monitor a set of PVs
pvs = ["chris:offset", "chris:amplitude"]
m = camonitor(pvs, print_update)

def on_button_clicked():
    def update(pv, textbox):
        value = textbox.text()
        try:
            if not value == "":
                caput(pv, float(value))
        except:
            print(f"Invalid value for {pv}:{value}")
    update("chris:freqCalc", on_button_clicked.callbacks['frequency'])
    update("chris:offset", on_button_clicked.callbacks['offset'])
    update("chris:amplitude", on_button_clicked.callbacks['amplitude'])

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        def createWidgets():
            graphWidget = pg.PlotWidget()
            frequency = {'textbox': QLineEdit(str(caget("chris:freqCalc"))),
                         'label':   QLabel('Frequency:')}
            offset =    {'textbox': QLineEdit(str(caget("chris:offset"))),
                         'label':   QLabel('Offset:')}
            amplitude = {'textbox': QLineEdit(str(caget("chris:amplitude"))),
                         'label':   QLabel('Amplitude:')}
            callbacks = {'frequency': frequency['textbox'],
                         'offset':    offset['textbox'],
                         'amplitude': amplitude['textbox']}
            widgets = [frequency, offset, amplitude]

            button = QPushButton('update')
            button.clicked.connect(on_button_clicked)
            on_button_clicked.callbacks = callbacks

            layout = QVBoxLayout()
            layout.addWidget(graphWidget)
            subLayout = QHBoxLayout()
            for widget in widgets:
                subLayout.addWidget(widget['label'])
                subLayout.addWidget(widget['textbox'])

            subLayout.addWidget(button)
            canvas = QWidget()
            self.setCentralWidget(canvas)
            canvas.setLayout(layout)
            panel = QWidget()
            layout.addWidget(panel)
            panel.setLayout(subLayout)
            graphWidget.setBackground('w')
            return graphWidget

        super(MainWindow, self).__init__(*args, **kwargs)
        frequency = PV("chris:freqCalc")
        offset = PV("chris:offset")
        amplitude = PV("chris:amplitude")
        frequency.put(0.5)
        offset.put(2.0)
        amplitude.put(3.0)
        graphWidget = createWidgets()

        self.x = list(range(-100,0))    # 100 time points
        self.y = [0.0]*100              # 100 amplitude values
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  graphWidget.plot(self.x, self.y, pen=pen)
    
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        def advance(l, newValue):
            l.append(newValue)
            return l[1:]
        self.x = advance(self.x, self.x[-1] + 1)
        self.y = advance(self.y, caget("chris:function"))
        self.data_line.setData(self.x, self.y)  # Update the data.

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    # allow all background tasks to run to completion.
    cothread.WaitForQuit()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    