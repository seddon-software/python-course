from math import sqrt
from decimal import *
import decimal

N = 104729 # prime
N = 227   # prime
N = 193*263*7
N = 331*101

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
print(f"N = {N}")
print(f"N = 331*101")
print(f"sqrt(N) = {N2}")
getcontext().prec = 2000

def factorialRange(lo, hi):
    result = 1
    for n in range(lo, hi+1):
        result = result * n
    return result
    
def factorial(n):
    result = 1
    for n in range(2, n+1):
        result = result * n
    return result

F = factorial(N2)
# F = factorial(350)

context = decimal.Context(prec=200000)
stage = 1

def homeIn(lo, hi):
    global stage
    F = factorialRange(2, N2) * factorialRange(lo, hi)
    X = Decimal(F) / Decimal(N)
    R = context.remainder(X, 1)
    if R == 0:
        stage += 1
    if stage == 1:
        hi = hi * 2
        homeIn(lo, hi)
    if stage == 2:
        delta = hi - lo
        lo += delta//2
        homeIn(lo, hi)
                     
    print(f"ans = {lo},{hi}")

#homeIn(N2, N2+10)
def check(lo, hi):
    F = factorialRange(2, N2) * factorialRange(lo, hi)
    X = Decimal(F) / Decimal(N)
    R = context.remainder(X, 1)
    return R == 0

def binarySearch(lo, hi, what):
    print(hi, lo)
    if check(lo, hi): return hi, lo
    hi = 2 * hi
    return binarySearch(lo, hi)    

x = binarySearch(N2, 2*N2)
print(x)






