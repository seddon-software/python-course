from math import sqrt
from decimal import *

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
print(f"Length of primes = {len(primes)}")
print(f"N = {N}")
getcontext().prec = 200

def inverse(x):
    return 1 / (x % 1)

def product(k):    
    F = 1
    for n in range(k):
        F = F * primes[n]
    return F

F = product(45)
print(f"F = Product of 45 primes = {F}")
X = Decimal(F)/Decimal(N)
print(f"F/N = {X}")
print(f"fraction_part(F/N) = {X%1}")
Z = 1/(X%1)
print(f"Z = inverse of fraction_part(F/N) = {Z}")
print(f"{F/(X*Z)}")
