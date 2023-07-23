'''
Size of dict
============

Dictionaries automatically grow as key,value pairs are added.  In this example we add successive key,value pairs
to a dictionary and print the size of the dictionary every time the size changes.  As you can observe, the 
dictionary starts with a small memory footprint and the doubles in size when it gets full.

Note that all keys need to be rehashed when the dictionary is resized; this is automatic, but does involve a
performance overhead.
'''

import sys

# start with an empty dictionary
d = {}

old_size = sys.getsizeof(d)
for i in range(100000):
    # keep adding key,value pairs of the form: key0:value0, key1:value1, key2:value2, etc 
    key = f"key{i}"
    value = f"value{i}"
    d[key] = value
    new_size = sys.getsizeof(d)
    # check for change in size
    if new_size > old_size:
        print(f"no of keys = {i} : bytes = {new_size}")
    old_size = new_size
