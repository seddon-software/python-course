'''
Unicode Properties
==================
Unicode characters all have a unique code point, but they also belong to a category and usually have a name.
Some characters also represent numbers in different scripts.  This example shows how to extract this information.
'''

import unicodedata

# create a string from unicode code points
u = chr(65) + chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231) + chr(0xf29) + chr(0x1F4A9)
print(u)

print(f"{'index':8s} {'code point':12s} {'category':10s}{' ':6s}{'name':>10s}") 

for i, c in enumerate(u):
    print(f"{i:3}: {ord(c):10X} {unicodedata.category(c):>10s}{' ':6s}{unicodedata.name(c)}")

# some unicode characters represent numbers (in this case, characters 2 and 6)
print(f"{u[2]} represents {int(unicodedata.numeric(u[2]))} in Tamil")
print(f"{u[6]} represents {int(unicodedata.numeric(u[6]))} in Tibetan")
