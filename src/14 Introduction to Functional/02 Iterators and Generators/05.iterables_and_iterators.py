import os; os.system("clear")
'''
Iterables and Iterators
=======================

Iterables are containers that can store multiple values and are capable of returning values one by one.

An iterator is an object of a class that has both of the methods:
            __iter__()
            __next__()

The iter() builtin function will create an iterator object from an iterable.  Here we create an iterator from 
a list.  

Note that the list is an "iterable" in the sense it has an __iter__() method (see below), but it is not
an iterator because it doesn't have a __next__() method.
'''

# note: a list is an iteratable (has __iter__ method), but not an iterator (no __next__ method)
array = [2, 3, 4, 5, 6, 7, 8]
print(f"array has __iter__ method: {hasattr(array, '__iter__')}")
print(f"array has __next__ method: {hasattr(array, '__next__')}")

i = iter(array)
print(f"i is of type {type(i)}")

# check that i has both iterator methods
print(f"i has an '__iter__' function: {hasattr(i, '__iter__')}")
print(f"i has an '__next__' function: {hasattr(i, '__next__')}")

for n in i:
    print(n, end=", ")
print()

