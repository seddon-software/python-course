array = [2, 3, 4, 5, 6, 7, 8]
i = iter(array)
print(i)

# check that i has both iterator methods
print("Does i have an '__iter__' function:", hasattr(i, "__iter__"))
print("Does i have an '__next__' function:", hasattr(i, "__next__"))

for n in i:
    print(n)
