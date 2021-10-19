# immutable variables
def addOne(x):
    x += 1
    return x

a = 100
a = addOne(a)
print(a)

# mutable variables
def addOneToAList(l):
    l[0] += 1

myList = [100, 200, 300]
addOneToAList(myList)
print(myList)
