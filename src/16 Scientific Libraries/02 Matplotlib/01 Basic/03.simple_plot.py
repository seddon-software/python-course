'''
Simple Plot
===========

To produce a simple plot, first create a figure with a set of axes.  Use 
            plt.subplot()

to do this.  This function only returns the axes and not the figure.  If you need to know the figure use:
            figure = plt.gcf()

The plot() method takes two arrays, one for x values and one for y values.  You can also pass a number of key
word args.
'''

import matplotlib.pyplot as plt

# object oriented interface uses axes 
ax = plt.subplot()      # create single figure with one axis
figure = plt.gcf()      # not used
color = "r"             # red
marker = "o"            # circle
redCircles = f"{color}{marker}"
ax.plot([1,2,3,4], [1,4,9,16], redCircles)
ax.axis([0, 6, 0, 20])
ax.set_ylabel("squares")
plt.show()

