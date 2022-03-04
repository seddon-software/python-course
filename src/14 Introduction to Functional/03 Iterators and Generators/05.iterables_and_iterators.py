'''
Iterables and Iterators
=======================

The iter() builtin function will create an iterator object from an iterable.  Here we create an iterator from 
a list.  

Note that the list is an "iterable" in the sense it has an __iter__() method (see below), but it is not
an iterator because it doesn't have a __next__() method.
'''

array = [2, 3, 4, 5, 6, 7, 8]
i = iter(array)
print(i)

# check that i has both iterator methods
print("Does i have an '__iter__' function:", hasattr(i, "__iter__"))
print("Does i have an '__next__' function:", hasattr(i, "__next__"))

for n in i:
    print(n, end=", ")
print()

# note: a list is an iteratable (has __iter__ method), but not an iterator (no __next__ method)
print("Does list have an '__iter__' function:", hasattr(array, "__iter__"))
print("Does list have an '__next__' function:", hasattr(array, "__next__"))

