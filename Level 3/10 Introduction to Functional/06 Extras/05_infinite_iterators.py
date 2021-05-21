import itertools

# these functions return infinite iterators
# once called they iterate forever

iter = itertools.count(10)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

iter = itertools.cycle('ABCD')
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

# this only iterates 3 times
iter = itertools.repeat(10, 3)
try:
    print(next(iter))
    print(next(iter))
    print(next(iter))
    print(next(iter))   # this fails
except:
    print("too many iterations")
