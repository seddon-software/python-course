'''
Timer decorator
===============

Write a "timer" decorator that calculates the time a function takes to execute.  THe decorator should be parametrised with a "count".
Call the decorated function multiple ("count") times and print the average execution time.  Take a look at the logging decorator to give you 
an idea of what to do.

The function being decorated may have arbitary parameters (possibly named), so you will need to use the pattern: fn(*args, **kwargs).  
I've given you some functions for you to decorate so you can test your decorator.
'''

import time

# define your decorator here
# def timer(count):

# test material below:
@timer(10)
def roots(n, power):
    '''finds the sum of the square roots of the first 'n' integers'''
    result = 0
    for i in range(n):
        result += i ** power
    return result

@timer(100)
def fib(n):
    '''calculates the n'th Fibonacci number without using a recursive formula'''
    a, b = 0, 1
    for _ in range(n):
        time.sleep(0.1)
        a, b = b, a + b
    return a

# call the decorator with positional parameters
print( f"{roots(10_000_000, 0.5):.4f}" )

# call the decorator with named parameters
print( f"{roots(n=10_000_000, power=0.5):.4f}" )

# try a different function
print(fib(30))