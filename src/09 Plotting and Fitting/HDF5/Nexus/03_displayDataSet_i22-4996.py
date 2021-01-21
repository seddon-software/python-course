import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# open Nexus file
f = h5py.File("data/i22-4996.nxs", "r")

# get dataset
ds = f["/entry1/Hotwaxs"]

# convert to numpy array
data = ds["data"][()]

# check shape (1,1,512)
print(data.shape)

# extract data as 1D array
X = data[0,0]
size = X.shape[0] 
Y = np.arange(size)

Xhat = savgol_filter(X, 51, 3) # window size 51, polynomial order 3
plt.plot(Y, X)
plt.plot(Y, Xhat)
plt.show()

