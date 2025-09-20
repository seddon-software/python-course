'''
Generator Comprehensions
========================

Generator comprehensions were covered earlier, but in this example we see they behave like a generator.  As
such they can be invoked with "next()" or be used in a loop as in:
            for r in roots:
                print("{0:6.2f}".format(r), end=' ')
            print()
'''


from math import sqrt

# generator expressions are comprehensions
# evaluate each expression on demand (lazy evaluation)


# use round brackets to return a generator expression (comprehension):
roots = (sqrt(x) for x in range(10))

# consume 3 values
print(f"{next(roots):6.2f}", end=' ')
print(f"{next(roots):6.2f}", end=' ')
print(f"{next(roots):6.2f}")

# iterate using the generator
# note: the generator has already been called 3 times
for r in roots:
    print(f"{r:6.2f}", end=' ')
print()




