import sys

'''
Add elements to a dictionary and print the 
size of the dictionary every time the size changes
'''

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
