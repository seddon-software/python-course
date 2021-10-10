from itertools import *


# these functions return infinite iterators
# once called they iterate forever

iter = count(10)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

iter = cycle('ABCD')
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

# this only iterates 3 times
iter = repeat(10, 3)
try:
    print(next(iter))
    print(next(iter))
    print(next(iter))
    print(next(iter))   # this fails
except:
    print("too many iterations")