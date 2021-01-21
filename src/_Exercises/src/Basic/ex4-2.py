"""
Write a function that rotates the values of an array.  For example:
    array = [100, 200, 300, 400, 500]
    Rotate( ... )
    # array is now: [200, 300, 400, 500, 100]
"""

def Rotate(a):
    start = a[0]
    a[:] = a[1:]
    a.append(start)

array = [100, 200, 300, 400, 500]

Rotate(array)
print(array)
