# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.animation import FuncAnimation
# Create a subplot
ROWS = 12
COLS = 8
fig, axis = plt.subplots(ROWS,COLS)
plt.subplots_adjust(bottom=0.35)

PLOTS = ROWS * COLS
gls = [1, 2, 3]
gls_Y = [2, 3, 4]

# convert axes from 2D to 1D
axis = axis.flatten()

for i in range(PLOTS):
    axis[i].plot(gls, gls_Y)

ax_value = plt.axes([0.25, 0.2, 0.65, 0.03])

slider = Slider(ax_value, 'Similarity', 0, PLOTS, valstep=1)


def update(frame, ax):
    global sliderValue
    if sliderValue > 0:
        axis[sliderValue-1].set_facecolor('yellow')

sliderValue = 0
def updateSliderValue(value):
    global sliderValue
    sliderValue = int(value)

slider.on_changed(updateSliderValue)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color='gold',
                hovercolor='skyblue')

def resetSlider(event):
    slider.reset()
    for n in range(PLOTS):
        axis[n].set_facecolor('red')

# Call resetSlider function when clicked on reset button
button.on_clicked(resetSlider)

ani = FuncAnimation(fig, update, frames=1000, fargs=(axis,), interval=100, blit=True)

# Display graph
plt.show()
