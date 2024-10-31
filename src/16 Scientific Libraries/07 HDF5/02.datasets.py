'''
Writing to a Dataset
====================

In this example we create a dataset and then write data to it.  We then see how to read the data back into memory.
When reading back data we can use the dataset provided the dataset is not closed, as in:
            readBack(fileName)

Recall the datset will be closed when we leave the "with" statement.  However in:
            readBack2(fileName)

we read the dataset as part of the "with" statement (before it is closed):
            dataset[:]

As an alternative, we can copy the dataset directly to a Numpy array with "[()]":
            data = dataset[()]      # copy to numpy array

In this case it is fine to close the dataset becuse the Numpy array is still in memory.
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
    # dataset now closed (and inaccessible)
    try:
        data = dataset[:]      # try to read entire array
        print(data)
    except Exception as e:
        print("dataset now closed (and inaccessible)")
        print(f"Error: {e}")

def readBack2(fileName):
    with h5py.File(fileName,'r') as file:
        dataset = file['/dset']
        print("Reading data back...")
        data = dataset[:]      # read entire array while dataset still open
        print(data)

def readBack3(fileName):
    with h5py.File(fileName,'r') as file:
        dataset = file['/dset']
        print("Reading data back...")
        data = dataset[()]      # copy to numpy array
    # dataset is now closed, but Numpy array is still in memory
    print(data)

fileName = 'data/mydataset.h5'
write(fileName)
readBack(fileName)          # this fails
readBack2(fileName)         # this works
readBack3(fileName)         # so does this
