'''
The memoize decorator is used to speed up recursive calculations by casching results of previous calculations.
This can greatly speed up recursive algorithms like Fibonacci where the same calculations are repeated many
times.

We can then profile our code and compare it to the previous example when memoize was not used.
'''
import profile


class memoize:
    def __init__(self, function):
        self.function = function
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = self.function(*args)
            return self.cache[args]

@memoize
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

def fibonacci_seq(n):
    seq = [ ]
    if n > 0:
        seq.extend(fibonacci_seq(n-1))
    seq.append(fib(n))
    return seq

print(fibonacci_seq(20))
profile.run('print(fibonacci_seq(20)); print()')


