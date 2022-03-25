'''
Creating Dataset
================

A dataset is a multidimensional array of data elements, together with supporting metadata.
'''

import h5py, os

if not os.path.exists('data'): os.mkdir('data')

file = h5py.File('data/dset.h5','w')

dataset = file.create_dataset("dset",(4, 6))        # must specify a size
print("Dataset dataspace is", dataset.shape)
print("Dataset Numpy datatype is", dataset.dtype)
print("Dataset name is", dataset.name)
print("Dataset is a member of the group", dataset.parent)
print("Dataset was created in the file", dataset.file)

file.close()
