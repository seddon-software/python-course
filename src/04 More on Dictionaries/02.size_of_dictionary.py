'''
Size of Dictionary
==================
The dict data stucture can become very large.  CPython reserves space for new entries, but periodically the
dict becomes full and needs to be resized.  

In this example we investigate when this happens; we sdd elements to a dictionary and print the size of the 
dictionary every time it changes.
'''

import sys

d = {}

old_size = sys.getsizeof(d)
for i in range(100000):
    key = f"key{i}"
    value = f"value{i}"
    d[key] = value
    new_size = sys.getsizeof(d)
    if new_size > old_size:
        print(f"no of keys = {i} : bytes = {new_size}")
    old_size = new_size
