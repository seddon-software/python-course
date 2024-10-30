import os; os.system("clear")
'''
Filter
======

filter(fn, sequence) takes two parameters
        fn          function returning boolean
        sequence    collection to be filtered
        return      items from the collection that return true when we call fn(item)

In this example the filter function removes numbers divisible by 2, 3, 5, 7, 11 and 13 (i.e. all the non primes).
'''

def primesFilter(x):
    if x % 2 == 0: return False
    if x % 3 == 0: return False
    if x % 5 == 0: return False
    if x % 7 == 0: return False
    if x % 11 == 0: return False
    if x % 13 == 0: return False
    return True

# set up a sequence
sequence = list(range(14, 200))

# filter out all non primes
primes = list(filter(primesFilter, sequence))
print(primes)




1
