'''
Filter
======

We've seen filter before, but this time we use filter with a lambda.
'''

sequence = [5, 7, 9, 2, 4, 6]
result = filter (lambda x: x > 4, sequence) 
print(list(result))