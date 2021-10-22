from math import sqrt

def square(x,y):
    sq = sqrt(x**2 + y**2)
    return sq

# print the bytecode in hex
bytecode = [ hex(x) for x in square.__code__.co_code]
print("\n".join(bytecode))

import dis
dis.dis(square)



