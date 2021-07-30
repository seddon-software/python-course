from timeit import timeit

# set up timers
from timeit import Timer
n = 10 * 1000 * 1000
ForLoop           = Timer('forLoop({})'          .format(n),'from __main__ import forLoop')
ForLoop2          = Timer('forLoop2({})'         .format(n),'from __main__ import forLoop2')
ListComprehension = Timer('listComprehension({})'.format(n),'from __main__ import listComprehension')
NumpyMethod       = Timer('numpyMethod({})'      .format(n),'from __main__ import numpy, numpyMethod')
C_Module          = Timer('cModule({})'          .format(n),'import _roots as roots; from __main__ import cModule')

print("results")
print(forLoop(n))
print(forLoop2(n))
print(listComprehension(n))
print(numpyMethod(n))
print(cModule(n))

# perform timings
count = 1
t1 = ForLoop.timeit(number=count)
t2 = ForLoop2.timeit(number=count)
t3 = ListComprehension.timeit(number=count)
t4 = NumpyMethod.timeit(number=count)
t5 = C_Module.timeit(number=count)

print("{:20s}{:>8s}{:>8s}".format("code", "time", "1/time"))
print("{:20s}{:>8s}{:>8s}".format("====", "====", "======"))
print("{:20s}{:8.3f}{:8.3f}".format("For Looop (v1)"     , t1, 1/t1))
print("{:20s}{:8.3f}{:8.3f}".format("For Looop (v2):"    , t2, 1/t2))
print("{:20s}{:8.3f}{:8.3f}".format("List Comprehension:", t3, 1/t3))
print("{:20s}{:8.3f}{:8.3f}".format("Numpy:"             , t4, 1/t4))
print("{:20s}{:8.3f}{:8.3f}".format("C Module"           , t5, 1/t5))


