############################################################
#
#    casts
#
############################################################

aTuple = (2, 3, 5, 7, 11, 13, 17, 19, 17, 19)
aList  = [2, 3, 5, 7, 11, 13, 17, 19, 17, 19]
aString = "ABCDEFGABC"

myList = list(aTuple)
print(myList)

myTuple = tuple(aList)
print(myTuple)

mySet = set(aTuple)
print(mySet)

myList = list(aString)
print(myList)

mySet = set(aString)
print(mySet)

