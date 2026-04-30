'''
Infinite Generators
===================

Because generators use lazy evaluation you can define infinite genertors.  Of course, in practice you will 
probably have a limit on the number of calls you make, but theoretically there is no limit.
'''
import itertools

def iterateLotsOfTimes(iter):
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print(next(iter), end=" ")
    print()


# these functions return infinite iterators
# they iterate forever
iter = itertools.count(10)
iterateLotsOfTimes(iter)

iter = itertools.cycle('ABCD')
iterateLotsOfTimes(iter)

# this raises an exception on the 4th call
iter = itertools.repeat(10, 3)
try:
    iterateLotsOfTimes(iter)
except:
    print("exception raised: only 3 iterations allowed")
