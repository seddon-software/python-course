def memoize(f):
    cache = {}
    def inner(n, k):
        if (n, k) in cache:
            return cache[(n, k)]
        else:
            cache[(n, k)] = f(n, k)
            return cache[(n, k)]
    return inner

# 1.8392867552141612
@memoize
def f(n, k):
    if n <= k: return 1
    result = 0
    for m in range(1, k+1):
        result += m*f(n-m, k)
    return result

for x in range(1, 70):
    print(x, f(200,x)/f(200-1,x))

import numpy as np
print(np.exp(1))
print((1+5**0.5)/2)
