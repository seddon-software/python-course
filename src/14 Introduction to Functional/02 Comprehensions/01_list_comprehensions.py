############################################################
#
#    comprehensions
#
############################################################

from math import sqrt

def cube(x):
    return x * x * x

# set up a sequence
sequence = list(range(1, 20))

# apply a comprehension to entire sequence
roots = [sqrt(x) for x in sequence]
n     = [   x    for x in sequence if x < 10 ]
cubes = [cube(x) for x in sequence if x%2==0 ]

print(roots)
print(n)
print(cubes)

# other examples
print([ x + y for x in range(1,13) for y in range(1,13) if x*y > 120])
print([(x,y) for x in range(1,13) for y in range(1,13) if x*y > 120])

# primes
n = 1000 #some arbitrary stopping point
primes = [p for p in range(2, n)
           if p not in
            [np for i in range(2, int(n**0.5) + 1)  # i = 2,3,..31 
                for np in range(i * 2, n, i)]]  # np = 4,6,8 .. + 6,9,12 .. + 8,12,16 .. + 10,15,20 ..
print(primes)

def isprime(num):
    return not [y for y in range(2,num) if num%y==0]

print([x for x in range(2,1000) if isprime(x)])

