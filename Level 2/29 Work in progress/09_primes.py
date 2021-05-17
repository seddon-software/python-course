import math
import matplotlib.pyplot as plt
import numpy as np

def getNormalizedFactors(n):
    # n2 is integer just above sqrt(n)
    n2 = math.sqrt(n);
    n2 = int(math.ceil(n2))
    
    for k in range(n2, n+1):
        a = n % k
        b = n // k
        # b and k are factors if a == 0 
        if a == 0:
            break
        # 
#    return f"{b:3d} * {k:3d} = {b*k}"
    return b, k

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


N = 100000
def isprime(num):
    return not [y for y in range(2,num) if num%y==0]

primes = [x for x in range(2,N) if isprime(x)]

Z = 33
pairs = [0]*Z

for prime in primes:
    for a in range(1, Z):
        if (prime - 2*a) in primes: pairs[a] += 1

X = range(1, Z)
Y = pairs[1:Z]
plt.plot(X, Y)
plt.show()

    