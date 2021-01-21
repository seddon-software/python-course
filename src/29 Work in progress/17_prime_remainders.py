from math import sqrt
from decimal import *
import decimal

# N = 104729 # prime
# N = 227   # prime
# N = 193*263*7
# N = 331*101
# N = 3*41
# A = 7
# B = 167
# N = A*B
N = 168
N2 = int(sqrt(N))

primes = [ 
      2,      3,      5,      7,     11,     13,     17,     19,     23,     29, 
     31,     37,     41,     43,     47,     53,     59,     61,     67,     71, 
     73,     79,     83,     89,     97,    101,    103,    107,    109,    113, 
    127,    131,    137,    139,    149,    151,    157,    163,    167,    173, 
    179,    181,    191,    193,    197,    199,    211,    223,    227,    229, 
    233,    239,    241,    251,    257,    263,    269,    271,    277,    281, 
    283,    293,    307,    311,    313,    317,    331,    337,    347,    349, 
    353,    359,    367,    373,    379,    383,    389,    397,    401,    409, 
    419,    421,    431,    433,    439,    443,    449,    457,    461,    463] 
#print(f"A = {A}, B = {B}, N = {N}, N2 = {N2}")
print(f"N = {N}, N2 = {N2}")
getcontext().prec = 2000

def factorialRange(lo, hi):
    result = 1
    for n in range(lo, hi+1):
        result = result * n
    return result
    
def factorial(n):
    result = Decimal(1)
    for n in range(2, n+1):
        result = result * Decimal(n)
    return result

context = decimal.Context(prec=200000)

def generateRemainders(N, N2):
    # note that there are duplicates for a lot of N
    results = []
    x = list(range(2, N2))

    for n in x:
        F = factorialRange(2, n)
        X = Decimal(F) / Decimal(N)
        R = context.remainder(X, 1)
        r = float(R)
        results.append(r)
    return results

for N in range(2, 200):
    N2 = int(sqrt(N))
    print(f"{N:4} {N2:3} {generateRemainders(N, N2)}")





