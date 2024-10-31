'''
Scatter Plot Sizes
==================

This is a simple script to illustrate different marker sizes.
'''
import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure("Marker Sizes")
ax = figure.add_subplot(1,1,1)



x = [0,2,4,6,8,10];         # draw markers equally spaced on x axis
y = np.zeros(len(x));       # all markers drawn on y = 0
s = [20*2**n for n in range(len(x))];   # vary the sizes
print(f"marker sizes: {s}")
ax.scatter(x,y,s=s)
plt.show()
