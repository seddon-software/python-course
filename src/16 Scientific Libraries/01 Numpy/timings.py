from timeit import timeit
import numba

def forLoop(n):
    _sum = 0
    for i in range(n):
        _sum += float(i)**0.5
    return _sum

def forLoop2(n):
    y = [0.0]*n
    for i in range(n):
        y[i] = float(i)**0.5
    return sum(y)

import math
def listComprehension(n):
    return sum([x**0.5 for x in range(n)])

import numpy
def numpyMethod(n):
    x = numpy.arange(0, n)
    y = numpy.sqrt(x)
    return numpy.sum(y)

@numba.jit(nopython=True, parallel=True)
def numbaMethod(n):
    x = numpy.arange(0, n)
    y = numpy.sqrt(x)
    return numpy.sum(y)

import _roots as roots
def cModule(n):
    return roots.sumOfRoots(n)

# set up timers
from timeit import Timer
n = 10 * 1000 * 1000
ForLoop           = Timer('forLoop({})'          .format(n),'from __main__ import forLoop')
ForLoop2          = Timer('forLoop2({})'         .format(n),'from __main__ import forLoop2')
ListComprehension = Timer('listComprehension({})'.format(n),'from __main__ import listComprehension')
Numpy             = Timer('numpyMethod({})'      .format(n),'from __main__ import numpy, numpyMethod')
C_Module          = Timer('cModule({})'          .format(n),'import _roots as roots; from __main__ import cModule')
Numba             = Timer('numbaMethod({})'      .format(n),'from __main__ import numpy, numbaMethod')


print("results")
print(forLoop(n))
print(forLoop2(n))
print(listComprehension(n))
print(numpyMethod(n))
print(numbaMethod(n))
print(cModule(n))

# perform timings
count = 1
t1 = ForLoop.timeit(number=count)
t2 = ForLoop2.timeit(number=count)
t3 = ListComprehension.timeit(number=count)
t4 = Numpy.timeit(number=count)
t5 = C_Module.timeit(number=count)
t6 = Numba.timeit(number=count)

print("{:20s}{:>8s}{:>8s}".format("code", "time", "t2/time"))
print("{:20s}{:>8s}{:>8s}".format("====", "====", "======="))
print("{:20s}{:8.3f}{:8.3f}".format("For Looop (v1)"     , t1, t2/t1))
print("{:20s}{:8.3f}{:8.3f}".format("For Looop (v2):"    , t2, t2/t2))
print("{:20s}{:8.3f}{:8.3f}".format("List Comprehension:", t3, t2/t3))
print("{:20s}{:8.3f}{:8.3f}".format("Numpy:"             , t4, t2/t4))
print("{:20s}{:8.3f}{:8.3f}".format("C Module"           , t5, t2/t5))
print("{:20s}{:8.3f}{:8.3f}".format("Numba:"             , t6, t2/t6))


