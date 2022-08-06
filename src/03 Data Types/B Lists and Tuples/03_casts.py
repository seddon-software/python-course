'''
casts
=====

Casts are used to create a copy of a collection that usually has a different type from the original.
'''

aTuple = (2, 3, 5, 7, 11, 13, 17, 19, 17, 19)
aList  = [2, 3, 5, 7, 11, 13, 17, 19, 17, 19]
aString = "ABCDEFGABC"

# convert tuple to a list
myList = list(aTuple)
print(myList)

# convert list to a tuple
myTuple = tuple(aList)
print(myTuple)

# convert tuple to a set
mySet = set(aTuple)
print(mySet)

# convert string to a list
myList = list(aString)
print(myList)

# convert string to a set (removes duplicates)
mySet = set(aString)
print(mySet)

# casting a list to another list creates a copy
aNewList = list(aList)
print(f"id of original: {id(aList)}")
print(f"id of copy:     {id(aNewList)}")
