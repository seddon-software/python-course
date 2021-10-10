"""
Write a function that rotates the values of 3 variables.  For example:
    x = 100
    y = 200
    z = 300
    Rotate( ... )
    # x is now 200
    # y is now 300
    # z is now 100
"""

def Rotate(a, b, c):
    return b, c, a

x = 100
y = 200
z = 300

x, y, z = Rotate(x, y, z)
print(x, y, z)
