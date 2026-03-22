'''
Timings
=======

This example compares several different approaches to computing the square roots of the first 10 million integers.
I've include a C example which needs to be built before you can run this example.  To build the C module, run the 
scripts in the "C_Library" folder.  If you prefer, you can exclude the C example by setting the boolean:
            EXCLUDE_C_EXAMPLE=True

Note that Numba runs on parallel CPUs and hence will be very fast; Numpy and C are similiar in speed.

Numba is a tool, created by members of the scientific Python community, that aims to leverage LLVM to allow selective compilation 
of pieces of a Python application to native machine code at runtime. It requires that LLVM be available on the system where the code 
is running, but can provide significant speed increases, especially for operations that are amenable to vectorisation.

Note the nested fstrings specifying formats as in:
            R = "20s"
            print(f"{'for loop:':{R}} {forLoop(n)}")
'''

EXCLUDE_C_EXAMPLE=False
EXCLUDE_CYTHON_EXAMPLE=False

import numpy
from timeit import timeit
import numba
import os

def forLoop(n):
    _sum = 0
    for i in range(n):
        _sum += float(i)**0.5
    return _sum

import math
def listComprehension(n):
    return sum([x**0.5 for x in range(n)])

import numpy
def numpyMethod(n):
    x = numpy.arange(0, n)
    y = numpy.sqrt(x)
    return numpy.sum(y)

'''
Numba translates Python functions to optimized machine code at runtime.
Numba will try to compile the code to a native binary (nopython mode), but will
produce errors when this is not possible
'''
@numba.jit(nopython=True, parallel=True)
def parallelNumpy_with_numba(n):
    x = numpy.arange(0, n)
    y = numpy.sqrt(x)
    return numpy.sum(y)

@numba.jit(nopython=True, parallel=False)
def numpy_with_numba(n):
    x = numpy.arange(0, n)
    y = numpy.sqrt(x)
    return numpy.sum(y)

if not EXCLUDE_C_EXAMPLE:
    import roots
    def cModule(n):
        return roots.sumOfRoots(n)

if not EXCLUDE_CYTHON_EXAMPLE:
    import cythonRoots
    def cythonModule(n):
        return cythonRoots.sumOfRoots(n)

# formats
N = "8.3f"
R = "20s"
T = "30s"
U = ">8s"

# set up timers
from timeit import Timer
n = 10 * 1000 * 1000
ForLoop           = Timer('forLoop(n)'          , 'from __main__ import n, forLoop')
ListComprehension = Timer('listComprehension(n)', 'from __main__ import n, listComprehension')
Numpy             = Timer('numpyMethod(n)'      , 'from __main__ import n, numpy, numpyMethod')
C_Module          = Timer('cModule(n)'          , 'from __main__ import roots, n, cModule')
Cython_Module     = Timer('cythonModule(n)'     , 'from __main__ import roots, n, cythonModule')
ParallelNumpy_with_Numba =  Timer('parallelNumpy_with_numba(n)'    , 'from __main__ import n, numpy, parallelNumpy_with_numba')
Numpy_with_Numba  = Timer('numpy_with_numba(n)'      , 'from __main__ import n, numpy, numpy_with_numba')

print("\nresults")
print("=======")
print(f"{'for loop:':{R}} {forLoop(n)}")
print(f"{'List Comprehension:':{R}} {listComprehension(n)}")
print(f"{'Numpy:':{R}} {numpyMethod(n)}")
print(f"{'Parallel Numba:':{R}} {parallelNumpy_with_numba(n)}")
print(f"{'Numpy with Numba:':{R}} {numpy_with_numba(n)}")
if not EXCLUDE_C_EXAMPLE: print(f"{'cModule:':{R}} {cModule(n)}")
if not EXCLUDE_CYTHON_EXAMPLE: print(f"{'cythonModule:':{R}} {cythonModule(n)}")
print()

# perform timings
count = 1
t1 = ForLoop.timeit(number=count)
t2 = ListComprehension.timeit(number=count)
t3 = Numpy.timeit(number=count)
if not EXCLUDE_C_EXAMPLE: t4 = C_Module.timeit(number=count)
if not EXCLUDE_CYTHON_EXAMPLE: t5 = C_Module.timeit(number=count)
t6 = ParallelNumpy_with_Numba.timeit(number=count)
t7 = Numpy_with_Numba.timeit(number=count)

print(f"{'code':{T}}{'time':{U}}{'t1/time':{U}}")
print(f"{'====':{T}}{'====':{U}}{'=======':{U}}")
print(f"{'For Loop (t1)':{T}}{t1:{N}}{t1/t1:{N}}")
print(f"{'List Comprehension':{T}}{t2:{N}}{t1/t2:{N}}")
print(f"{'Numpy':{T}}{t3:{N}}{t1/t3:{N}}")
if not EXCLUDE_C_EXAMPLE: 
    print(f"{'C Module':{T}}{t4:{N}}{t1/t4:{N}}")
if not EXCLUDE_CYTHON_EXAMPLE: 
    print(f"{'Cython Module':{T}}{t5:{N}}{t1/t5:{N}}")
print(f"{'Parallel Numpy with Numba':{T}}{t6:{N}}{t1/t6:{N}}")
print(f"{'Non Parallel Numpy with Numba':{T}}{t7:{N}}{t1/t7:{N}}")
print(f"No of CPUs = {os.cpu_count()}")

