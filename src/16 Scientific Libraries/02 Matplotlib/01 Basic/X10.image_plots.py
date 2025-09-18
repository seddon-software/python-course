'''
Image Plots
===========

You can manipulate images with Numpy and MatPlotLib.  For a start you can read an image into a Numpy array with: 
            img = mpimg.imread('macy_parade.jpg')

The Numpy array is 3 dimensional; the x and y dimensions and a color dimension.  With the "Macy Parade" image the
array size is:
            (1536, 2048, 3)

and the pixel values are integers in the range 0..255.  Once we have the image as a Numpy array we can take slices
to see parts of the image.

We can view the red part of the image using the colormap "gray":

            subImage = img[500:700, 1200:1700, 1]
            plt.imshow(subImage, cmap='gray', vmin=0, vmax=255)
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# show whole image
plt.figure("Macy Parade")
img = mpl.image.imread('macy_parade.jpg')
print(f"Image dimensions: {img.shape}")
print(type(img))
print(img)
plt.imshow(img)

# show sub-image
plt.figure("Sub Image")
subImage = img[500:700, 1200:1700, :]
print(f"Image dimensions: {subImage.shape}")
plt.imshow(subImage)

# show single color with cmap switched to greyscale
plt.figure("Single Color (red) Image")
subImage = img[500:700, 1200:1700, 1]
print(f"Image dimensions: {subImage.shape}")
plt.imshow(subImage, cmap='gray', vmin=0, vmax=255)

plt.tight_layout()
plt.show()

