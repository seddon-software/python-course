'''
Reduce
======

Here we use reduce with a lambda.  

1. reduce() starts by applying the function to the first two elements of the iterable.
2. the result is used as the first argument for the next call, along with the next element from the iterable.
3. this continues until all elements have been processed

reduce (lambda 2,3:      2*3,    2,3,4,5,6,7,8)
reduce (lambda 6,4:      6*4,      6,4,5,6,7,8)
reduce (lambda 24,5:    24*5,       24,5,6,7,8)
reduce (lambda 120,6:  120*6,        120,6,7,8)
reduce (lambda 720,7:  720*7,          720,7,8)
reduce (lambda 5040,8:5040*8,           5040,8)
reduce (lambda        :40320,            40320)
'''

from functools import reduce

product = reduce (lambda x, y: x*y, [2,3,4,5,6,7,8])
print(product)

