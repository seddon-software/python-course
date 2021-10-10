import numpy as np


array = np.fromfunction(lambda i,j: 10*i+j, (10,10), dtype = int)
print("array=\n", array)

row_indices = [4, 5, 6]
print("row_indices:\n", array[row_indices])

col_indices = [3, 4, 5]
print("col_indices:\n", array[:,col_indices])

indices = [0, 11, 22, 33, 44, 55]   # array is treated as 1 dimensional
print("take:\n", array.take(indices))
print("take:\n", np.take(array, indices))

indices = [5, 4, 3, 4, 5, 4, 5, 4, 5, 4]   # choose selects from 5th of col 0, 4th of col 1, 3rd of col 2 ...
print("choose:\n", np.choose(indices, array))

print("array=\n", array)
print("row and col indices:\n", array[[9, 8, 7], [9, 8, 7]]) # selects [9,9], [8,8], [7,7]
print("diag:\n", np.diag(array))
print("diag with offset:\n", np.diag(array, -3))

