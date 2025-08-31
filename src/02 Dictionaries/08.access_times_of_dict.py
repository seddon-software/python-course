'''
Dictionary Access Times
=======================
Dictionaries (hash tables) are popular because of fast lookups.  In fact the lookup time in a dictionary
is constant, independent of the number of entries in the dictionary.  We illustrate this fact by using the timeit
module in the code below:
'''

import sys, timeit
from random import randint


def setupDictionary(n):
    d = {}
    for i in range(n):
        # keep adding key,value pairs of the form: key0:value0, key1:value1, key2:value2, etc 
        key = f"key{i}"
        value = f"value{i}"
        d[key] = value
    return d

d = {}
statements = []
result = None

def timeDictionaryAccess(N):
    global d, statements, result   # make these variables visible to timeit via globals()
    d = setupDictionary(N)
    if N == 10:
        print(f"dictionary looks like: {d}") 

    statements = []
    randomKeys = []
    for n in range(N):
        # pick a random key
        randomKey = f"key{randint(0, N)}"
        # and build a list of lookups based on random keys 
        statements.append(f"v = d['{randomKey}']")    # statement to access a random key

    # use the timeit module to see how long the lookups take
    times = timeit.timeit(setup=f'N={N}', stmt='for i in range(N):statements[i]', number=1000, globals=globals())
    # as N increases, so we perform more lookups, so we need to divide by N to get average times
    print(f"average access time with {N} items: {times/N:.6f}")

timeDictionaryAccess(10)
timeDictionaryAccess(50)
timeDictionaryAccess(100)
timeDictionaryAccess(500)
timeDictionaryAccess(1000)
timeDictionaryAccess(5000)
timeDictionaryAccess(10000)
timeDictionaryAccess(50000)
timeDictionaryAccess(100000)
timeDictionaryAccess(500000)
timeDictionaryAccess(1000000)
   
