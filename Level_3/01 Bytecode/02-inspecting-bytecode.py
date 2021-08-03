from math import sqrt

def square(x,y):
    sq = sqrt(x**2 + y**2)
    return sq

print(square.__code__)
print([ hex(x) for x in square.__code__.co_code] )

import dis
dis.dis(square)



