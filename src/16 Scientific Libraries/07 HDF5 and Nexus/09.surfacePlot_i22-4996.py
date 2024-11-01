'''
Here we look at a 3 dimensional plot of data contained in a Nexus file
'''

import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# open Nexus file
f = h5py.File("data/i22-4996.nxs", "r")

# get dataset
ds = f["/entry1/Rapid2D"]

# convert to numpy array
data = ds["data"][()]

# check shape (1,1,512,512)
print(f"original shape: {data.shape}")

# extract data as 2D array
image = data[0,0]

cropped_image = image[260:280, 195:230]
print(f"cropped shape: {cropped_image.shape}")
X = np.arange(cropped_image.shape[1])
Y = np.arange(cropped_image.shape[0])
X, Y = np.meshgrid(X, Y) 
print(f"shape of X data: {X.shape}")
print(f"shape of Y data: {Y.shape}")


fig = plt.figure()
fig.canvas.manager.set_window_title("i22-4996.nxs")
ax = fig.add_subplot(projection='3d')
ax.set_title("surface plot of Rapid2D")
surface = ax.plot_surface(X, Y, cropped_image, cmap='terrain')

plt.show()

