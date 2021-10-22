import sys, timeit
from random import randint

'''
Create a dictionary of various sizes and then time accessing an element of the dictionary
This should be constant, independent of size
'''

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
    if N == 10: print(d)     # get an idea of what the dictionary looks like
    randomKey = f"key{randint(0, N)}" 
    statement = f"v = d['{randomKey}']"    # statement to access a random key
    print(f"access time for d['{randomKey}'] with {N} items: {timeit.timeit(statement, globals=globals()):.3f}")

timeDictionaryAccess(10)
timeDictionaryAccess(100)
timeDictionaryAccess(1000)
timeDictionaryAccess(10000)
timeDictionaryAccess(100000)
timeDictionaryAccess(1000000)
timeDictionaryAccess(10000000)
    
