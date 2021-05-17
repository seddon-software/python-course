from itertools import *

def doit(iter):
    for x in iter:
        print(x, end=' ')
    print()


doit( product('ABCD', repeat=3) )
doit( permutations('ABCD', 2) )
doit( combinations('ABCDE', 3) )
doit( combinations_with_replacement('ABCD', 2) )


1
