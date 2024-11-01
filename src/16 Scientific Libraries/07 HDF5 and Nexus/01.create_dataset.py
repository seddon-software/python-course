'''
Creating Datasets
=================

Hierarchical Data Format (HDF) is a set of file formats (HDF4, HDF5) designed to store and organize large amounts of data. Originally developed at the 
U.S. National Center for Supercomputing Applications, it is supported by The HDF Group, a non-profit corporation whose mission is to ensure continued 
development of HDF5 technologies and the continued accessibility of data stored in HDF. 

Central to HDF is the concept of a dataset.  A dataset is a pointer to data stored on disk.  The idea behind datasets is that data is only read into memory
when a component of the dataset is read or written.  Typically, we store (Numpy) multidimensional arrays of data elements on disk, together with supporting metadata.

In this chapter we investigate the key aspects of datasets, but realise that real world examples will involve much larger datasets than our examples.
HDF5 files can contain multiple datasets.  They are arranged like a file system, but contained in a single file.

Here we create a dataset (4 x 6 array) but don't write to it.  Nevertheless space is allocated for the array on the disk.
'''

import h5py, os

if not os.path.exists('data'): os.mkdir('data')

def write(fileName):
    with h5py.File(f'{fileName}','w') as file:
        dataset = file.create_dataset("dset",(4, 6))        # must specify a size
        print("Dataset dataspace is", dataset.shape)
        print("Dataset Numpy datatype is", dataset.dtype)
        print("Dataset name is", dataset.name)
        print("Dataset is a member of the group", dataset.parent)
        print("Dataset was created in the file", dataset.file)

fileName = 'data/mydataset.h5'
write(fileName)
