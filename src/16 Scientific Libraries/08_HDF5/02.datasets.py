'''
Writing to a Dataset
====================

In this example we create a dataset and then write data to it.  We then see how to read the data back into memory.
'''

import h5py
import numpy as np

def write(fileName):
    file = h5py.File(fileName,'w')
    file.create_dataset("dset",(4, 6))
    dataset = file['/dset']
    print("Writing data...")
    dataset[...] = np.arange(1, 25).reshape(4,6)    
    file.close()

def readBack(fileName):
    file = h5py.File(fileName,'r')
    dataset = file['/dset']
    print("Reading data back...")
    data = dataset[()]
    print(data)
    file.close()

fileName = 'data/dset.h5'
dataset = '/dset'
write(fileName)
readBack(fileName)
