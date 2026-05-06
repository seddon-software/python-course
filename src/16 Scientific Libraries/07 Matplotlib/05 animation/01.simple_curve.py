'''
This example draws a curve plotted with N values of x and y, where each y = x**2
The list x starts as [0,1,2,3...N-1]
the list y starts as [0,1,4,9...(N-1)**2] 
The update routine changes the x and y values using the frame variable (which increases by one on each call)
Thus successive values of x are:
    frame = 0   [1,2,3,4,...N]
    frame = 1   [2,3,4,5...N+1]
    frame = 2   [3,4,5,6...N+2]
etc.
update is called every 100 msec and the whole animation restarts after 400 frames
    
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Creating a figure and axis
fig, ax = plt.subplots(figsize=(7, 4))


N = 20      # number of points in curve

# Generating x values 
x = list(range(N))
y = [i**2 for i in x]

# Plotting the initial curve
line, = ax.plot(x, y)
ax.set_xlim([-1.0, N**2])
ax.set_ylim([-1.0, N**4])

# Function to update the plot for each frame of the animation
def update(frame):
    print(frame, end=",")           # so you can see it repeat every 400 frames
    x = list(range(frame,frame+N))
    y = [i**2 for i in x]
    # update the artist
    line.set_xdata(x)
    line.set_ydata(y)
    return line         # return the artist (not required in this case because blit by default is False)

# Creating a FuncAnimation object
ani = animation.FuncAnimation(fig=fig, func=update, frames=400, interval=100)

# Displaying the output
plt.show()
