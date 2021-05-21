sequence = list(range(1, 10))
result = [(lambda x: x**2)(x) for x in sequence if x > 5]
print(result)
