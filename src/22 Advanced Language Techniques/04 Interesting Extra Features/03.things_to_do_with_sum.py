'''
Things to do with sum
=====================
The sum() builtin is design to sum numbers, but it can also flatten lists.  sum can take a maximum of two 
parameters.  Some examples are given below
'''

# sum will add up a list
first = [5, 6, 7]     # just a single parameter
print(sum(first))

try:
    result = sum(5, 6, 7)     # doesn't work with more than 2 parameters
    print(result)
except Exception as e:
    print(e)

# sum will add up elements in its first argument and add to its second 'scalar' argument
first = [5, 6, 7]
second = 100
print((sum(first, second)))

# if the second argument is a list, the first argument is flattened and append to the second argument
first = [[1, [2, 3]], [4, 5], [6], [[7, 8], 9]]
second = ['abc', 'def']
print((sum(first, second)))

# this fails
try:
    first = [5, 6, 7]
    second = [100, 200]
    print((sum(first, second)))  # first parameter must be 2D sequence
except Exception as e:
    print(e)

# if the second argument is an empty list, sum will flatten a 2D list
first = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
second = []
print(sum(first, second))
