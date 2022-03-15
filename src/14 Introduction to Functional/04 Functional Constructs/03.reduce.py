'''
Reduce
======

reduce(fn, sequence) takes two parameters
        fn          function (mapping) to apply to each item in the sequence
        sequence    collection to be mapped
        return      modified collection

The reduce function is used to successively apply a function to elements of the sequence in such a way that
the sequence is reduced in size until the whole sequence has been processed.
'''

from functools import reduce

# find the sum of numbers 1 .. 10
numbers = list(range(1, 11))
sum = reduce(lambda x, y: x + y, numbers, 0)
print(sum)


# look at the general case
def fn(a, b):
    print(f"a={a}, b={b}")
    return f"({a}+{b})"

result = reduce(fn, ["S1", "S2", "S3", "S4", "S5"])
print(f'reduce(fn, ["S1", "S2", "S3", "S4", "S5"] = {result}')

