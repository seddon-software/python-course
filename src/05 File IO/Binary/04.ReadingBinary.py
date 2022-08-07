'''
The array module is more efficient than struct and should be used for formatting large amounts binary data.
The struct module provides finer control for smaller data sets.

This time we work with a larger file (created earlier).  Note "stat" is used to read the file size information
from the inode, so we know how big a buffer to create in memory.
'''

import array
import os

def readBinary(filename):
    try:
        size = os.stat(filename).st_size        # reads inode to find file size
        with open(filename, "rb") as f:
            ints = array.array('B')      # sets up a unsigned integer buffer
            ints.fromfile(f, size)       # populates the buffer
            theList =ints.tolist()       # convert to list of ints
    except Exception as e:
        print(e)
    return theList

intList = readBinary('data/myfile-4.bin')

print(("{:>10s}{:>10s}".format("Decimal", "Hex")))
for i in intList:
    print(("{:10d}{:>10s}".format(i, hex(i))))
