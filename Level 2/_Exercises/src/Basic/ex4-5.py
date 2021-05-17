"""
Write a function that takes an integer list as a parameter 
and doubles the value of each element of the array.
"""

def DoubleIt(theList):
    for i, item in enumerate(theList):
        theList[i] *= 2

myList = [2, 3, 5, 7, 11, 13, 17, 19]
DoubleIt(myList)
print(myList)

