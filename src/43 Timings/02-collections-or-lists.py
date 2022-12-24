'''
The timeit module provides a simple way to time Python code fragments. It is usually best to make mutltiple calls
to the code fragment and measure the average time of execution.

The timeit constructor is defined as:
            timeit.timeit(stmt, setup, timer, number=??)

where
            stmt        = statement under test
            setup       = code to be run once before timing the code fragment
            timer       = which timer to use (usually defaulted)
            number      = number of calls made to test code fragment

The timeit module does not have direct access to the symbol table of the calling program, so it is common practice
to import necessary modules as part of the setup.

In the example we compare timings for 100, 1000 and 10000 iterations to see the effect of multiple calls.
'''

from timeit import timeit

def runit(title, stmt, setup, count):
    t = timeit(f'{stmt}', f'{setup}', number=count)
    print(f"count={count:<6}: {title} {t/count:0.10f}")

for count in 100, 1000, 5000, 10000, 100000:
    runit("collections", "s.appendleft(100)", "import collections; s = collections.deque()", count)

for count in 100, 1000, 5000, 10000, 100000:
    runit("lists      ", "s.insert(0,100)", "s = []", count)
