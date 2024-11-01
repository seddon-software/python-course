import os; os.system("clear")
'''
Color Art
=========
Here the same "art" image, but this time in color.  Have fun!
'''

import copy
import scipy.ndimage as nd
import matplotlib.pyplot as plt
from skimage import color
from skimage import img_as_float


import skimage.io as io
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4), dpi=72*3)
fig.canvas.set_window_title("Chris Seddon in Colour")
image = io.imread("images/chris.jpg", as_gray=True)
t1 = 0.33
t2 = 0.49
t3 = 0.72
image = color.gray2rgb(image)
image2 = copy.copy(image)
image2[image[:,:,0] <= t1] = (0.25, 0.20, 0.40)#(0.25, 0.20, 0.20)
image2[(image[:,:,0] > t1) & (image[:,:,0] <= t2)] = (0.70, 0.20, 0.20)
image2[(image[:,:,0] > t2) & (image[:,:,0] <= t3)] = (0.90, 0.80, 0.20)
image2[ image[:,:,0] > t3] = (0.99, 0.99, 0.40)

plt.axis('off')
ax.imshow(image2)
plt.savefig("out/chris_in_color.pdf")
plt.show()
