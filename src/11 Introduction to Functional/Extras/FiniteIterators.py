from itertools import *


def doit(iter):
    for x in iter:
        print(x, end=' ')
        if x == 30: break
    print()
    
# combine the arguments in series
doit( chain("ABCDEF", "1234") )

# filter items corresponding to the list of booleans in second arguments
doit( compress([1,2,3,4,5,6], [True, False, False, True, False, True]) )

# drop items in sequence while condition is true, but return all elements 
# thereafter even if condition becomes true again
doit( dropwhile(lambda x: x<5, [1,4,6,4,1,10,5,8]) )

# split a single iterable into several identical ones
iter1, iter2, iter3 = tee([1,2,3,4,5], 3)
doit(iter1)
doit(iter2)
doit(iter3)
