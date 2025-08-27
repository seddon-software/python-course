'''
Sparse Arrays
=============
It is unusual to have int keys when using a dictionary.  However, such keys allow you to optimise storage
of a sparse array.  In the exaple below we compare a dictionary with 3 int keys with an equivalent list
that spans a similar range of indices.

The sparse hash is much smaller than it's list counterpart.
'''

import sys

# set up a dictionary with 'int' keys and tuples as values
hash = { 
            2507: ('Red', 'Green', 'Blue'),
             672: ('Black', 'White', 'Grey'),
            3496: ('Orange', 'Purple', 'Yellow')
       }

print(f"hash[672] = {hash[672]}")
print(f"size of hash = {sys.getsizeof(hash)} bytes")

# compare with list
sparseList = [None]*3500
sparseList[2507] =('Red', 'Green', 'Blue'),
sparseList[672] = ('Black', 'White', 'Grey'),
sparseList[3496] = ('Orange', 'Purple', 'Yellow')
print(f"sparseList[672] = {sparseList[672]}")
print(f"size of sparse list = {sys.getsizeof(sparseList)} bytes")

# the sparse dictionary doesn't have an index of 2845
try:
    print(f"hash[2845] = {hash[2845]}")
except KeyError as e:
    print("Key error with hash: " + str(e))

# the sparse array does have an index of 2845
try:
    print(f"sparseList[2845] = {sparseList[2845]}")
except KeyError as e:
    print("Key error: " + str(e))
