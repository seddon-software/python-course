# cython: language_level=3

cdef extern from "<math.h>":
        double sqrt(double)

def sumOfRoots(int n):
    cdef int i
    cdef double sum
    sum = 0.0;
    for i in range(n):
        sum += sqrt(float(i))
    return sum;

