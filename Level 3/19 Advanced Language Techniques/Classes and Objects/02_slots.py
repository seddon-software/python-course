# class with slots do NOT have a dictionary
#   and this can be problematical for using this class with library code.
# The attributes in __slots__ are the only data attributes allowed

class Point(object):
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

