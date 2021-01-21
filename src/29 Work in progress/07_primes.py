import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.interpolation import shift
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


def isprime(num):
    return not [y for y in range(2,num) if num%y==0]

N = 100
primes = [n for n in range(2,N**2) if isprime(n)]

aboves = []
for p in primes:
    above = getNormalizedFactors(p-1)
    below = getNormalizedFactors(p+1)
    both = (above[0], above[1], below[0], below[1])
    if (above[1] - above[0] == 3) and (below[1] - below[0] == 1):
        print(p, above[0])
        aboves.append(above[0])


range_ = set(range(2,N))
aboves = set(aboves)
missing = range_.difference(aboves)   
print(missing)
    
 