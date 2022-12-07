'''
Infinite Generators
===================

Generator functions that never return give rise to infinite generators.  These generators called by called
for ever.  In this example we use next() to get numbers from the generator.  Note the generator runs for ever
and never gets reset.
'''

def powers(x):
    while(True):
        x = x * 2
        yield x

# create the infinite generator, initialized with 55
g = powers(55)

x = 0
while x < 1000:
    x = next(g)
    print(x, end=", ")
print()
    
for n in range(1000):
    print(next(g), end=", ") 
print()
       
