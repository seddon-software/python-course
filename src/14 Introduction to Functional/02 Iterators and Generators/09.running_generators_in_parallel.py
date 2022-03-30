'''
Running Generators in Parallel
==============================

Generators suspend execution when you hit a "yield" statement.  We can make use of this feature to allow us
to run several generators in parallel.  Working this way we can running concurrent code in a single thread.
This is essentially how the new "asyncio" library works.
'''

import time

def squares():
    n = 1
    while True:
        yield n**2
        n += 1

def cubes():
    n = 1
    while True:
        yield n**3
        n += 1
        
def quads():
    n = 1
    while True:
        yield n**4
        n += 1

# create 3 generators and put them in a list
generators = []
generators.append( squares() )
generators.append( cubes() )
generators.append( quads() )

# generators allow us to perform different calculations in parallel without using threading
# create a round robin scheduler with the list of generators
while(True):
    for g in generators:
        print(next(g))
        time.sleep(0.5)

