import numpy as np


array = np.fromfunction(lambda i,j: (i+2)*(j+2), (4,4))
print(array, "\n")

# overwrite row 2
array[2,] = 99
print(array, "\n")

# overwrite col 2
array[:,2] = 77
print(array, "\n")
