'''
Python distribution provides two profilers for measuring execution time of various functions.

    cProfile - It's an extension of C hence adds reasonably low overhead to actual code when performing profiling.
    profile - It’s totally written in python hence adding a reasonable amount of overhead to actual code when performing profiling.

This example explores using the profile module.
'''

import profile

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

def fibonacci_seq(n):
    ''' use recursion to capture the Fibonacci sequence in a list'''
    seq = [ ]
    if n > 0:
        seq.extend(fibonacci_seq(n-1))
    # recursion will reverse the order of calculations, insuring fib(0) is calculated first
    seq.append(fib(n))
    return seq

print(fibonacci_seq(20))
profile.run('print(fibonacci_seq(20)); print()')


