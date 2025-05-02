'''
Customized Colormap
===================
In this example I've used the results from the previous example to select suitable parameters for the image.
I've then defined a customized colormap (very faint colors) that can be used to print the image on paper such 
that you can use the image as the basis of a pencil drawing (it is very like tracing the image faintly).
'''

import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import skimage.feature as feature
import skimage.io as io
from PIL import Image
from matplotlib.colors import ListedColormap

def createColorMap():
    N = 2
    vals = np.ones((N, 4))
    # colormap goes from nearly white to white
    vals[:, 0] = np.linspace(0.85, 1, N)
    vals[:, 1] = np.linspace(0.85, 1, N)
    vals[:, 2] = np.linspace(0.85, 1, N)
    return ListedColormap(vals)

def plotIt(image, outImage, sigma, threshold, spread, dt):
    low = threshold / 256.0
    high = (threshold + spread) / 256.0
    set_title(f"sigma={sigma} low={low*256} high={high*256}")
    edges = feature.canny(image, sigma=sigma, low_threshold=low, high_threshold=high)
    edges = np.invert(edges)
    plt.imshow(edges, cmap=createColorMap())
    plt.draw()
    plt.axis('off')
    plt.savefig(outImage)

def set_title(title):
    figure = plt.gcf()
    figure.canvas.manager.set_window_title(title)

def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

image = io.imread("images/chris.jpg", as_gray=True)


sigma = 2
threshold = 29
spread = 1
plotIt(image, "out/chris_edges.pdf", sigma, threshold, spread, dt=0)
plt.show()

