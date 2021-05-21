def memoize(f):
    cache = {}
    def inner(n):
        # print("{}: {}".format(n, cache))
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
print( f"with memoize: {timeit.timeit(stmt='fib(8)', setup='from __main__ import fib', number=1000000)}" )
print( f"using recursion: {timeit.timeit(stmt='Fib(8)', setup='from __main__ import Fib', number=1000000)}" )
