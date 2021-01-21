"""
Write a function that takes two int arrays (of the same size) as parameters 
and adds the arrays together, element by element.  Return the summed array.
"""

def AddArrays(array1, array2):
    result = []
    for i, item in enumerate(array1):
        result.append(array1[i] + array2[i])
    return result


a1 = ( 3,  6,  9, 10, 20, 17, 14)
a2 = (17, 14, 11, 10,  0,  3,  6)

result = AddArrays(a1, a2)
print(result)