############################################################
#
#    generator expressions
#
############################################################

from math import sqrt

# generator expressions are comprehensions
# evaluate each expression on demand (lazy evaluation)

# use round brackets to return a generator expression (comprehension):
roots = (sqrt(x) for x in range(10))

# iterate using the generator
for r in roots:
    print("{0:6.2f}".format(r), end=' ')
print()


# comprehensions behave like generator expressions (but are evaluated immediately)
roots = [sqrt(x) for x in range(10)]
for r in roots:
    print("{0:6.2f}".format(r), end=' ')
print()


