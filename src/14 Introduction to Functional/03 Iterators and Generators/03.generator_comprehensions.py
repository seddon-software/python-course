'''
Generator Comprehensions
========================

Generator comprehensions were covered earlier, but in this example we see they behave as a generator.  As
such they can be invoked with "next()" or be used in a loop as in:
            for r in roots:
                print("{0:6.2f}".format(r), end=' ')
            print()
'''


from math import sqrt

# generator expressions are comprehensions
# evaluate each expression on demand (lazy evaluation)

# use round brackets to return a generator expression (comprehension):
roots = (f"{sqrt(x):6.2f}" for x in range(10))

# consume 3 values
print(next(roots))
print(next(roots))
print(next(roots))

# iterate using the generator
# note: the generator has already been called 3 times
for r in roots:
    print(r, end=' ')
print()




