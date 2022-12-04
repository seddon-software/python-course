'''
Map
===

We've seen map before, but this time we use map with a lambda.
'''

sequence = [5, 7, 9, 2, 4, 6]
result = map(lambda x: x*x, sequence) 
print(list(result))
