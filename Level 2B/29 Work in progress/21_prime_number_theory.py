from math import log, exp, sqrt
from decimal import *

getcontext().prec = 200
N = 1000
N2 = int(sqrt(N))
L = log(N)

print(L)

def getLog(n):
    x = Decimal(n).ln()
    while x < L:
        x += Decimal(n).ln()
    return x

logOfFactors = sum([getLog(n) for n in range(2, 33)])
print(f"logOfFactors = {logOfFactors}")

for x in range(2, 100):
    c = (logOfFactors - Decimal(x).ln()).exp()
    ci = Decimal.to_integral_value(c)
    print(x, +Decimal(c-ci))
    