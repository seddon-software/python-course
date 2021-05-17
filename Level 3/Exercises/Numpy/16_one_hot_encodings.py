'''
Create a 1D array of random ints of size (30,) containing only the numbers
10, 11, 12, 13 or 14. Now create 30 'one hot encodings' for the original array.
For example a set of 'one hot encodings' for:
    [20, 22, 21, 22, 20, 22]
would be:
    [1 0 0]
    [0 0 1]
    [0 1 0]
    [0 0 1]
    [1 0 0]
    [0 0 1]
'''
def one_hot_encodings(arr):
    unique = np.unique(arr)
    out = np.zeros((arr.shape[0], unique.shape[0]))
    for i, k in enumerate(arr):
        out[i, list(unique).index(k)] = 1
    return out

import numpy as np
a = np.random.randint(low=10, high=15, size=(30,)); print(a)
hot = one_hot_encodings(a)
print(hot)
