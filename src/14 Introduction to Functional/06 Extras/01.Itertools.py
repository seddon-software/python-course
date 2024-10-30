import os; os.system("clear")
'''
Iteratools
==========

The itertools module provides a number of utility routines to perform functional tasks.  Here we look at a few
of these routines:
    1) chain():      combines iterators into a single iterator
    2) compress():   filters items from the first iterable
    3) dropwhile():  removes items from the first iterable while a condition is true
    4) tee():        splits an iterable into several iterables
'''

from itertools import chain, compress, dropwhile, tee


def doit(iter):
    for x in iter:
        print(x, end=' ')
    print()
    
# combine the iterators in series
doit( chain("ABCDEF", "1234") )

# filter items corresponding to the list of booleans in second arguments
doit( compress([1,2,3,4,5,6], [True, False, False, True, False, True]) )

# drop items in sequence while condition is true, but 
# return all elements thereafter even if condition becomes true again
doit( dropwhile(lambda x: x<5, [1,4,6,4,1,10,5,8]) )

# split a single iterator into several identical ones
iter1, iter2, iter3 = tee([1,2,3,4,5], 3)
doit(iter1)
doit(iter2)
doit(iter3)
