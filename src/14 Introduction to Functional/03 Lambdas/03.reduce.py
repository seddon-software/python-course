import os; os.system("clear")
'''
Reduce
======

We've seen reduce before, but this time we use reduce with a lambda.
'''

from functools import reduce

sequence = list(range(1, 10))
product = reduce (lambda x, y: x*y, sequence)
print(product)

