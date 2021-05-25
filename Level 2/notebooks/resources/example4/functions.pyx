# cython: language_level=3

def say_hello():
    print("say_hello was compiled using cython")

def say_goodbye():
    print("say_goodbye was compiled using cython")

def fibonacci(int n):
    cdef int a, b
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

def sumOfSquares(int lo, int hi):
    cdef int n
    cdef double sum
    sum = 0.0
    for n in range(lo, hi + 1):
        sum += n**1.1
    return sum
