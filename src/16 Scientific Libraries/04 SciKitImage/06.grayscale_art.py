'''
Grayscale Art
=============
This is a bit of fun. I've just used the previous image and filled in areas with greyscales to create some "art".
'''

import os, sys
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import skimage.morphology as morphology
import skimage.feature as feature
from PIL import Image
import time


import skimage.io as io
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4), dpi=72*3)
fig.canvas.set_window_title("Chris Seddon in Black and White")
image = io.imread("images/chris.jpg", as_gray=True) * 256
t1 = 90
t2 = 116
t3 = 154

image[image < t1] = 0
image[(image > t1) & (image <= t2)] = t2
image[(image > t2) & (image <= t3)] = t3
image[image > t3] = 255

plt.axis('off')
ax.imshow(image, cmap=plt.cm.gray)
plt.savefig("out/chris_in_gray.pdf")
plt.show()
