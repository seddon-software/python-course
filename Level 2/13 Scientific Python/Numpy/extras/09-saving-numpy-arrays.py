import numpy as np
import os
np.set_printoptions(precision=3)

# create a 2D matrix
matrix = np.fromfunction(lambda i,j: (i+2)**2.3 + (j+2)**1.3, (8,5))
print(matrix)
print("----------------")

# save to text file in a particular format
np.savetxt("files/my-matrix.csv", matrix, delimiter = "; ", fmt='%8.4f')
os.system("cat files/my-matrix.csv")
print("----------------")

# save in numpy's native format
np.save("files/my-matrix", matrix)
os.system("cat files/my-matrix.csv")
print("----------------")

# read it back
data = np.load("files/my-matrix.npy")
print(data)

