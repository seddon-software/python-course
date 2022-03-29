'''
With HDF5 data can be arranged in groups and sub-groups.  These are very much like directories in the filesystem.
The idea is that large datafiles can be split into groups and then individual groups loaded into memory without
the need to read in the whole file.

With very large files (from experiments) it would be very inconvenient to read the entire file into memory.  In
fact this is one of the main objectives of HDF5 - being able to load subsets of data into memory.  The groups and
subgroups effectively create a "filesystem within a file".

This time we create an array attribute in the dataset "MyGroup/MySubGroup/my_dset".  After creating the HDF5 file 
we read it back into memory.

In the next example, we use a command line utility to check the contents of the file.
'''

import h5py
import numpy as np

def write(fileName):
    file = h5py.File(fileName,'w')
    group = file.create_group("MyGroup")
    subgroup = group.create_group("MySubGroup")
    print("Writing data...")
    ds = subgroup.create_dataset("my_dset", (4, 6))
    ds[...] = np.arange(101, 125).reshape(4,6)    
    file.close()
    
def readBack(fileName):
    file = h5py.File(fileName,'r')
    subgroup = file['/MyGroup/MySubGroup']
    print("Reading data back...")
    data = subgroup['my_dset'][()]
    print(data)
    file.close()

fileName = 'data/dset.h5'
write(fileName)
readBack(fileName)
