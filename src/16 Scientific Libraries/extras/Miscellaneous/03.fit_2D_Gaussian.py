import os; os.system("clear")
'''
This example analyses a 2 dimensional gaussian stored in a TIF file.  We use unicode variables throughout.
'''

import scipy.optimize as opt
import numpy as np
from numpy import sin, cos, exp
import pylab as plt
import PIL
from scipy.optimize import curve_fit

def load_image(fileName):
    image = PIL.Image.open(fileName)
    image.load()
    return np.asarray(image, dtype="float")


def twoD_Gaussian(xdata_tuple, amplitude, xo, yo, σₓ, σᵧ, ϑ, offset):
    (x, y) = xdata_tuple
    a = cos(ϑ)**2/(2*σₓ*σₓ) + sin(ϑ)**2/(2*σᵧ*σᵧ)
    b = -sin(2*ϑ)/(4*σₓ*σₓ) + sin(2*ϑ)/(4*σᵧ*σᵧ)
    c = sin(ϑ)**2/(2*σₓ*σₓ) + cos(ϑ)**2/(2*σᵧ*σᵧ)
    g = offset + amplitude*exp(-(a*(x-xo)**2 + 2*b*(x-xo)*(y-yo) + c*(y-yo)**2))
    g = g.transpose()
    return g.ravel()

def getResult(p):
    return (f"amp={p[0]:.2f}, xo={p[2]:.2f}, yo={p[1]:.2f}",
            f"σₓ={p[4]:.2f}, σᵧ={p[3]:.2f}, ϑ={p[5]:.2f}, offset={p[6]:.2f}");

def initial_guess():
    amplitude = 3
    xo = 100
    yo = 100
    σₓ = 20
    σᵧ = 40
    ϑ = 0
    offset = 10
    return (amplitude, xo, yo, σₓ, σᵧ, ϑ, offset)

fileName = "data/gaussian.tif"
image = load_image(fileName)
data = image[()]

minX, minY = 300, 800
sizeX, sizeY = 215, 200
maxX, maxY = minX+sizeX, minY+sizeY
data_raw = data[minX:maxX, minY:maxY]
#sizeX, sizeY = data_raw.shape
# Create x and y indices
x = np.arange(0, sizeX)
y = np.arange(0, sizeY)
x, y = np.meshgrid(x, y)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 8))
plt.gcf().canvas.manager.set_window_title('2D Gaussian Fitting')
ax1.set_title("raw 2D Gaussian")
ax2.set_title("fitted 2D Gaussian")

popt, pcov = opt.curve_fit(twoD_Gaussian, (x, y), np.ravel(data_raw), p0=initial_guess())

data_fitted = twoD_Gaussian((x, y), *popt)
print(getResult(popt))
ax2.imshow(data_raw.reshape(sizeX, sizeY), cmap=plt.cm.jet)
ax2.contour(y.transpose(), x.transpose(), data_fitted.reshape(sizeX, sizeY), 4, colors='w')



ax1.imshow(data_raw)
plt.text(25, 170, getResult(popt)[0], bbox=dict(facecolor='yellow', alpha=0.5), fontsize=12)
plt.text(25, 185, getResult(popt)[1], bbox=dict(facecolor='yellow', alpha=0.5), fontsize=12)
plt.show()
