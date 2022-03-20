'''
Access Times of Dictionary
==========================
The dict data structure is implemented in CPython as a hash table.  Hash tables are really fast.  The 
access time to retreive an item from a hash is independent of the size of the hash.  This is nomally represented
as searching in O(1) time (i.e. constant time).

Here we check this out by creating dictionaries of various sizes and then time accessing a random
element of the dictionary.
'''

import sys, timeit


def setupDictionary(n):
    d = {}
    for i in range(n):
        key = f"key{i}"
        value = f"value{i}"
        d[key] = value
    return d

d = {}
def timeDictionaryAccess(N):
    global d
    d = setupDictionary(N)
    statement = f"""v = d['key{N//2}']"""
    print(f"{N:8} {timeit.timeit(statement, globals=globals()):.3f}")

print(f'{"size":>8} {"access time"}')
timeDictionaryAccess(      10)
timeDictionaryAccess(      50)
timeDictionaryAccess(     100)
timeDictionaryAccess(     500)
timeDictionaryAccess(    1000)
timeDictionaryAccess(    5000)
timeDictionaryAccess(   10000)
timeDictionaryAccess(   50000)
timeDictionaryAccess(  100000)
timeDictionaryAccess(  500000)
timeDictionaryAccess( 1000000)
timeDictionaryAccess( 5000000)
timeDictionaryAccess(10000000)
    
