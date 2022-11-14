array = list(range(10, 30))   # this is a list (mutable)
mytuple = tuple(range(10, 30)) #  this is also a type of array (immutable)
print(mytuple)
mytuple[3] = 88
array.append(99)
print(array)
print(array[2])
print(array[-1])
print(array[5:15])

