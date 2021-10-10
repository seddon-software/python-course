import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.interpolation import shift
import numpy as np
from sympy.ntheory.generate import prime

def getNormalizedFactors(n):
    # n2 is integer just above sqrt(n)
    n2 = math.sqrt(n);
    n2 = int(math.ceil(n2))
    
    for k in range(n2, n+1):
        a = n % k
        b = n // k
        # b and k are factors if a == 0 (k >= b)
        if a == 0:
            break
        # 
#    return f"{b:3d} * {k:3d} = {b*k}"
    return b, k

N = 10000

def isprime(num):
    return not [y for y in range(2,num) if num%y==0]

primes = [x for x in range(2,N) if isprime(x)]
# for prime in primes:
#     print(prime)
    
factors = {}
for n in range(1, N):
    b, k = getNormalizedFactors(n)
#    print(f"{b} * {k} = {n}")
    factors[n] = (b, k)
# print(factors)

def checkIfLargestFactorOfNumberABitLessThanAPrimeIsItselfPrime(offset):
    for prime in primes:
        try:
            b, k = factors[prime-offset]
            # why am i getting repeats? please investigate
            # I get repeats whatever value of offset I use
            # if we look at the prime-offset, its largest factor is probably prime
            print(f"{prime:4}: {factors[prime-offset]}, {factors[k]}")
        except:
            pass

def checkIfLargestFactorOfNumberABitLessThanNIsItselfPrime(numbers, offset):
    for number in numbers:
        try:
            b, k = factors[number-offset]
            # why am i getting repeats? please investigate
            # I get repeats whatever value of offset I use
            # if we look at the prime-offset, its largest factor is probably prime
            print(f"{number:4}: {factors[number-offset]}, {factors[k]}")
        except:
            pass

checkIfLargestFactorOfNumberABitLessThanAPrimeIsItselfPrime(4)
numbers = list(range(N))
checkIfLargestFactorOfNumberABitLessThanNIsItselfPrime(numbers, 0)
