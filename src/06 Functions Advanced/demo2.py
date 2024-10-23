def average(*args):            # pack parameters
    return sum(args)/len(args)

print(average(6, 8, 12))
print(average(6, 8, 12, 15))
myList = [6, 8, 12, 15]
print(average(*myList))     # unpack parameters
