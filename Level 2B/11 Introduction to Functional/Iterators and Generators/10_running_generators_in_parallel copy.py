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

generators = []
generators.append( squares() )
generators.append( cubes() )
generators.append( quads() )

# generators allow us to perform different calculations in parallel
# create a round robin scheduler
while(True):
    for g in generators:
        print(next(g))
        time.sleep(0.5)

