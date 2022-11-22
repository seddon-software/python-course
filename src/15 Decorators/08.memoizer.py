'''
Memoizer
========

This is a decorator that is used to reduce the number of calls in a recursive function.  Here we apply it to
a Fibonacci function, but it can be applied to any recursive function.

The idea is that the first time a recursive function of depth n is called, the result is stored in a cache.  When
future calls are made, the cache is checked to see if the call has been calculated before, in which case the cached
value is used, otherwise the calculation is performed and the new result is placed in the cache.

It can be surprising how many recursive calls are made if we don't use a cache.  Here we compare timings using 
the cache (the memoize decorator) with the recursion without the cache for n == 6 and n ==8, by repeating the calculation
1,000,000 times.  As n increases the non memoizer case becomes incredibly slow, but the memoize case remains
fast.
'''

def memoize(f):
    cache = {}
    def inner(n):
        # print(f"{n}: {cache}")
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return inner

@memoize
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

def Fib(n):
    return n if n < 2 else Fib(n-1) + Fib(n-2)

import timeit, sys
sys.setrecursionlimit(20000)  
print( f"with memoize fib(6): {timeit.timeit(stmt='fib(6)', setup='from __main__ import fib', number=1000000):.2f}" )
print( f"without memoize fib(6): {timeit.timeit(stmt='Fib(6)', setup='from __main__ import Fib', number=1000000):.2f}" )
print( f"with memoize fib(8): {timeit.timeit(stmt='fib(8)', setup='from __main__ import fib', number=1000000):.2f}" )
print( f"without memoize fib(8): {timeit.timeit(stmt='Fib(8)', setup='from __main__ import Fib', number=1000000):.2f}" )
