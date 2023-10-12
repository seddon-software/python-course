'''
This example shows a typical design of a class.  Classes are quite complicated and this example needs a full
explanation.  Therefore I've given full details in the accompanying Jupyter Notebook (see the 
python-notebooks section).
'''

class Point:
    '''
    this is a simple class that has 3 methods
    '''
    def __init__(self, name, x0 = 0, y0 = 0):
        '''
        this is the constructor - its called automatically
        '''
        self.name = name
        self.x = x0
        self.y = y0
    
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def display(self):
        print("Point {} is at ({},{})".format(self.name, self.x, self.y))
        
# create objects
q = Point('origin')
p1 = Point('point-1', 100, 200)
p2 = Point('point-2', 200, 300)
p3 = Point('point-3', 300, 500)

# inspect the hidden dunder attributes for the class
print(Point.__dict__)
print(Point.__bases__)

# inspect the hidden dunder attributes for an object
print(p1.__dict__)
print(p1.__class__)

# call methods
p1.moveBy(1, 1)
p2.moveBy(2, 3)
p3.moveBy(3, 6)
p1.display()
p2.display()
p3.display()


