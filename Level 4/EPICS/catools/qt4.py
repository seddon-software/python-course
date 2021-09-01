import sys


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot

def on_button_clicked():
    textbox = on_button_clicked.z
    textboxValue = textbox.text()
    print(textboxValue)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')
graphWidget = pg.PlotWidget()
#window.setCentralWidget(graphWidget)

hour = [1,2,3,4,5,6,7,8,9,10]
temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
graphWidget.plot(hour, temperature)
textbox = QLineEdit()
textbox.move(20, 20)
textbox.resize(280,40)

button = QPushButton('update')
button.clicked.connect(on_button_clicked)
on_button_clicked.z = textbox
layout = QHBoxLayout()

layout.addWidget(textbox)
layout.addWidget(button)
# layout.addWidget(QPushButton('Left'))
# layout.addWidget(QPushButton('Center'))
# layout.addWidget(QPushButton('Right'))
layout.addWidget(graphWidget)

window.setLayout(layout)



window.show()

sys.exit(app.exec_())

