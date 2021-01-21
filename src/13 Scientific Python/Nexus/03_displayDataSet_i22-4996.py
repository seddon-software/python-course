import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


# open Nexus file
f = h5py.File("data/i22-4996.nxs", "r")

# get dataset
ds = f["/entry1/Hotwaxs/data"]

# check shape (1,1,512)
print(f"dataset shape = {ds.shape}")

# extract last dimension to numpy array
Y = ds[(0,0)]
size = Y.shape[0] 
X = np.arange(size)
# window size 51, polynomial order 3
Y_filtered = savgol_filter(Y, 51, 3) 


ax = plt.gca()
ax.set_title("i22-4996.nxs")
ax.set_xlabel("X")
ax.set_ylabel("Hotwaxs")
plt.plot(X, Y)
plt.plot(X, Y_filtered)
plt.show()
