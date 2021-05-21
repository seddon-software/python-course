# nested list comprehensions are useful for multi-dimenional arrays
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


cubes = [[col**3 for col in row] for row in matrix]
print(cubes)
