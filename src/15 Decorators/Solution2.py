'''
Timer decorator
===============

Write a "timer" decorator that calculates the time a function takes to execute.  THe decorator should be parametrised with a count.
Call the decorated function "count" times and print the average execution time.

The function being decorated may have arbitary parameters (possibly named), so you will need to use: fn(*args, **kwargs).  
I've given you some functions for you to decorate so you can test your decorator.
'''

import time

def timer(count):
    def decorator(func):
        def enhance(*args, **kwargs):
            start = time.time()
            for n in range(count):
                result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__}{args}: takes {(end - start)/count:.4f}s")
            return result
        return enhance
    return decorator

@timer(10)
def roots(n, power):
    '''finds the sum of the square roots of the first 'n' integers'''
    result = 0
    for i in range(n):
        result += i ** power
    return result

print( f"{roots(10_000_000, 0.5):.4f}" )
print( f"{roots(n=10_000_000, power=0.5):.4f}" )

@timer(100)
def fib(n):
    '''calculates the n'th Fibonacci number without using a recursive formula'''
    a, b = 0, 1
    for _ in range(n):
        time.sleep(0.1)
        a, b = b, a + b
    return a

print(fib(30))