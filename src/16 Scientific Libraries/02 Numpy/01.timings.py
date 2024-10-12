'''
Timings
=======

This example compares several different approaches to computing the square roots of the first 10 million integers.
I've include a C example which needs to be built before you can run this example.  To build the C module, run the 
scripts in the "C_Library" folder.  If you prefer, you can exclude the C example by setting the boolean:
            EXCLUDE_C_EXAMPLE=True

Note that Numba runs on parallel CPUs and hence will be very fast; Numpy and C are similiar in speed.
'''

EXCLUDE_C_EXAMPLE=False

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
def parallelNumba(n):
    x = numpy.arange(0, n)
    y = numpy.sqrt(x)
    return numpy.sum(y)
@numba.jit(nopython=False, parallel=False)
def numbaMethod(n):
    x = numpy.arange(0, n)
    y = numpy.sqrt(x)
    return numpy.sum(y)

if not EXCLUDE_C_EXAMPLE:
    import roots
    def cModule(n):
        return roots.sumOfRoots(n)

@numba.jit(nopython=True, parallel=False)
def forLoopWithNumba(n):
    _sum = 0
    for i in range(n):
        _sum += float(i)**0.5
    return _sum


# set up timers
from timeit import Timer
n = 10 * 1000 * 1000
ForLoop           = Timer('forLoop(n)'          , 'from __main__ import n, forLoop')
ForLoop2          = Timer('forLoop2(n)'         , 'from __main__ import n, forLoop2')
ListComprehension = Timer('listComprehension(n)', 'from __main__ import n, listComprehension')
Numpy             = Timer('numpyMethod(n)'      , 'from __main__ import n, numpy, numpyMethod')
C_Module          = Timer('cModule(n)'          , 'from __main__ import roots, n, cModule')
ParallelNumba     = Timer('parallelNumba(n)'    , 'from __main__ import n, numpy, parallelNumba')
Numba             = Timer('numbaMethod(n)'      , 'from __main__ import n, numpy, numbaMethod')
ForLoopWithNumba  = Timer('forLoopWithNumba(n)' , 'from __main__ import n, numpy, forLoopWithNumba')

print("\nresults")
print("=======")
print(f"{'forLoop:':20s} {forLoop(n)}")
print(f"{'forLoop2:':20s} {forLoop2(n)}")
print(f"{'listComprehension:':20s} {listComprehension(n)}")
print(f"{'numpyMethod:':20s} {numpyMethod(n)}")
print(f"{'parallelNumba:':20s} {parallelNumba(n)}")
print(f"{'numbaMethod:':20s} {numbaMethod(n)}")
if not EXCLUDE_C_EXAMPLE: print(f"{'cModule:':20s} {cModule(n)}")
print(f"{'forLoopWithNumba:':20s} {forLoopWithNumba(n)}")
print()

# perform timings
count = 1
t1 = ForLoop.timeit(number=count)
t2 = ForLoop2.timeit(number=count)
t3 = ListComprehension.timeit(number=count)
t4 = Numpy.timeit(number=count)
if not EXCLUDE_C_EXAMPLE: t5 = C_Module.timeit(number=count)
t6 = ParallelNumba.timeit(number=count)
t7 = Numba.timeit(number=count)
t8 = ForLoopWithNumba.timeit(number=count)

print("{:20s}{:>8s}{:>8s}".format("code", "time", "t2/time"))
print("{:20s}{:>8s}{:>8s}".format("====", "====", "======="))
print("{:20s}{:8.3f}{:8.3f}".format("For Loop (v1)"     ,  t1, t2/t1))
print("{:20s}{:8.3f}{:8.3f}".format("For Loop (v2):"    ,  t2, t2/t2))
print("{:20s}{:8.3f}{:8.3f}".format("List Comprehension:",  t3, t2/t3))
print("{:20s}{:8.3f}{:8.3f}".format("Numpy:"             ,  t4, t2/t4))
if not EXCLUDE_C_EXAMPLE: 
    print("{:20s}{:8.3f}{:8.3f}".format("C Module"       ,  t5, t2/t5))
print("{:20s}{:8.3f}{:8.3f}".format("Parallel Numba:"    ,  t6, t2/t6))
print("{:20s}{:8.3f}{:8.3f}".format("Non Parallel Numba:",  t7, t2/t7))
print("{:20s}{:8.3f}{:8.3f}".format("For Loop with Numba:", t8, t2/t8))


