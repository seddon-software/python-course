'''
Combinatorial Generators
========================

The itertools module has several methods for generating combinations.
'''

from itertools import *

def doit(iter):
    for x in iter:
        print(x, end='')
    print()
    print()


# find all possible combinations taking one character from 'ABC' with 
# one character from another 'ABC'
doit( product('ABC', 'ABC') )
doit( product('ABC', repeat=2) )    # equivalent to previous example

# find all 2 letter permutations of characters from 'ABCD'
doit( permutations('ABCD', 2) ) # order matters
doit( combinations('ABCD', 2) ) # order does not matter

# characters are not normally repeated ...
doit( combinations('ABCDE', 3) )

# ... unless you use this
doit( combinations_with_replacement('ABCDE', 3) )



