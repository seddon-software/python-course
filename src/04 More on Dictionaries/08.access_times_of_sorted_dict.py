'''
Unlike C++, Python has very few built in container classes, namely list and dict.  If you require a different
type of container that scales well, consider using "sortedcontainers":
            https://grantjenks.com/docs/sortedcontainers

Sorted containers is an open-sourced library that allows us to insert or delete elements very efficiently and 
the elements maintaining a sorted order. Sorted Containers is an Apache2 licensed sorted collections library, 
written in pure-Python, and fast as C-extensions.

The library contains three containers:
            SortedList 
            SortedDict 
            SortedSet

You can install sorted collection by the pip command:
            sudo pip install sortedcontainers 

For a detailed discussion of the efficiency of these containers refer to the authors docs:
            https://grantjenks.com/docs/sortedcontainers/performance-scale.html

This benchmark shows that the SortedDict search times are similar to the Python dict (about 10% slower).
'''

import sys, timeit
from sortedcontainers import SortedDict


def setupDictionary(n):
    d = SortedDict({})
    for i in range(n):
        key = f"key{i}"
        value = f"value{i}"
        d[key] = value
    return d

d = SortedDict({})
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
    
