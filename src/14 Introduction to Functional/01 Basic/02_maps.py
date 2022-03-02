'''
map(fn, sequence) takes two parameters
        fn          function (mapping) to apply to each item in the sequence
        sequence    collection to be mapped
        return      modified collection

In these examples the mapping function is (i) sqrt (ii) square.  The mapping is applied to all items in the
sequence.
'''

from math import sqrt

def cube(x):
    return x * x * x


# set up a sequence
sequence = list(range(1, 20))

# apply a map to entire sequence
roots = list(map(sqrt, sequence))
for value in roots:
    print("%6.2f" % value, end=' ') 
print()

cubes = list(map(cube, sequence))
for value in cubes:
    print("%6i" % value, end=' ') 
print()

1
