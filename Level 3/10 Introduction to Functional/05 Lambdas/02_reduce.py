from functools import reduce

sequence = list(range(1, 10))
product = reduce (lambda x, y: x*y, sequence)
print(product)

