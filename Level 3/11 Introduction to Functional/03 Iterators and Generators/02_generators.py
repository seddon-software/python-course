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
g = powers()
print(g)

# check that g has both iterator methods
print("Does g have an '__iter__' function:", hasattr(g, "__iter__"))
print("Does g have an '__next__' function:", hasattr(g, "__next__"))


# check the identity of the generator object
print(f"{id(g):x}")
# check the identity of the object returned by __iter__()
i = g.__iter__()
print(f"{id(i):x}")

# call __next__
print(g.__next__())
print(g.__next__())

# use the global function next
print(next(g))
print(next(g))

# use g in a loop as an iterator
for n in powers():
    print(n)
    
