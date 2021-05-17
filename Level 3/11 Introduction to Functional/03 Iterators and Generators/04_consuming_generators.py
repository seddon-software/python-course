############################################################
#
#    generators
#
############################################################

from math import sqrt

roots = (sqrt(x) for x in range(10))

print(sum(roots))   # consume the generator
print(sum(roots))   # the generator is now empty







