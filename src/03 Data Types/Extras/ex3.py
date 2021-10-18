x = [2, 3, 5]   # x points at a list
y = x           # y points at the same list

print(id(x))
print(id(y))
x[1] = 99       # lists are MUTABLE, so we can change the list
print(id(x))
print(id(y))

print(x)
print(y)
