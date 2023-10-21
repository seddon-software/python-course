'''
Writing to a Dataset
====================

In this example we create a dataset and then write data to it.  We then see how to read the data back into memory.
'''

import h5py
import numpy as np

def write(fileName):
    with h5py.File(fileName,'w') as file:
        file.create_dataset("dset",(4, 6))
        dataset = file['/dset']
        print("Writing data...")
        dataset[...] = np.arange(1, 25).reshape(4,6)    

def readBack(fileName):
    with h5py.File(fileName,'r') as file:
        dataset = file['/dset']
        print("Reading data back...")
        data = dataset[()]      # copy to numpy array
        print(data)

fileName = 'data/dset.h5'
dataset = '/dset'
write(fileName)
readBack(fileName)
