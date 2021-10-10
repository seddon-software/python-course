############################################################
#
#    generators
#
############################################################

# functions that contain yield return an iterator
# by calling said function

def powers():
    x = 1
    while(x < 1000):
        x = x * 2
        yield x
        pass        # just to show execution resumes after the yield
    return

# calling the function produces a generator object, which is also an iterator
# note: calling the function does NOT execute the code in the function
g = powers()
print(g)

# check that g has both iterator methods
print("Does g have an '__iter__' function:", hasattr(g, "__iter__"))
print("Does g have an '__next__' function:", hasattr(g, "__next__"))

# look at all the methods
print(dir(g))

# check the identity of the generator object
print(f"{id(g):x}")
# check the identity of the object returned by __iter__() is the same
i = g.__iter__()
print(f"{id(i):x}")

# call __next__ directly (discouraged)
print(g.__next__())
print(g.__next__())

# use the global function next (recommended)
print(next(g))
print(next(g))

# use g in a loop as an iterator (not the call powers() to instantiate the generator)
for n in powers():
    print(n)
    
