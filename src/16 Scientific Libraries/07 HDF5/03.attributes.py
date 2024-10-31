'''
One of the important features of HDF5 is the ability to attach attributes to datasets.  At Diamond these 
attributes are generated automatically during experiments.

In this example we add a 4x6 array to a dataset, a string attribute to say what "Units" we are working in and a "Speed" attribute containing a Numpy array
consisting of 2 elements [100, 200].

Just to make sure things worked, we read the HDF5 file back into memory.
'''

import h5py
import numpy as np

def write(fileName):
    file = h5py.File(fileName,'w')
    file.create_dataset("dset",(4, 6))
    dataset = file['/dset']
    dataset.attrs["Units"] = "Meters per second"
    dataset.attrs.create("Speed", np.array([100,200]))
    file.close()


def readBack(fileName):
    # read attributes back and print them
    with h5py.File(fileName,'r') as file:
        dataset = file['/dset']
        print(f"keys = {dataset.attrs.keys()}")
        print("Reading data back...")
        for k,v in dataset.attrs.items():
            print(f"key={k}, value={v}")

fileName = 'data/mydataset.h5'
write(fileName)
readBack(fileName)
