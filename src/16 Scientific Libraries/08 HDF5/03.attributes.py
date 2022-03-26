'''
One of the important features of HDF5 is the ability to attach attributes to datasets.  At Diamond these 
attributes are generated automatically during experiments.

In this example we add a 4x6 array to a dataset, a string to say what "Units" we are working in and a "Speed".
Just to make sure things worked, we read the HDF5 file back into memory
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
    # read attrs back and print it
    file = h5py.File(fileName,'r')
    dataset = file['/dset']
    z = dataset.attrs.keys()
    print("Reading data back...")
    for k,v in dataset.attrs.items():
        print(f"key={k}, value={v}")
    file.close()

fileName = 'data/dset.h5'
write(fileName)
readBack(fileName)
