'''
Slots were introduced as a performance boost for classes.  They are not often used.

Classes using slots do NOT have a dictionary, instead the permitted attributes are deined by:
            __slots__ = ('x', 'y')

The class will not permit adding futher attributes and __dict__ doesn't exist.  Most library code assumes classes
have a dictionary to store their attributes; this can be problematical for using such classes with library code.
'''


class Point(object):
    # The attributes in __slots__ are the only data attributes allowed
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("x, y = ", self.x, self.y)        

p = Point(10, 20)
p.display()
p.x = 50
p.y = 50
try: print(p.__dict__)
except: print("dictionary does not exist")

try: p.z = 50
except: print("attribute not allowed")

