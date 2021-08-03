# sum will add up elements in its first argument
print((sum([5, 6, 7])))

# sum will add up elements in its first argument and add to its second argument
print((sum([5, 6, 7], 100)))

# if the second argument is a list, the first argument is flattened and append to the second argument
l = [[1, [2, 3]], [4, 5], [6], [[7, 8], 9]]
print((sum(l, ['abc', 'def'])))

# if the second arguent if an empty list, sum will flatten a 2D list
l = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(("----->", sum(l, [])))
