############################################################
#
#    maps
#
############################################################

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
