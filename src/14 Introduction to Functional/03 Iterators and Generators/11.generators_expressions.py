'''
Generator Expressions
=====================

This example is an alternative way of running generators in parallel.  This time we use generator comprehensions.
'''

import time

N = 10
generators = [(n**2 for n in range(N)),
              (n**3 for n in range(N)),
              (n**4 for n in range(N))]

# generators allow us to perform different calculations in parallel
# create a round robin scheduler
while(True):
    try:
        for g in generators:
            print(next(g), end=", ")
            time.sleep(0.5)
    except StopIteration as e:
        break
print()
