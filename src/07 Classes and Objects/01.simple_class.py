'''
This example show a typical design of a class.  Classes are quite complicated and this example needs a full
explanation.  Therefore I've given full details in the accompanying Jupyter Notebook (see the 
python-notebooks section).
'''


class Point:
    '''
    put documentation in here
    '''
    def __init__(self, name, x0 = 0, y0 = 0):
        '''
        put documentation in here
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
print(Point.__dict__)
print(Point.__bases__)
print(p1.__dict__)
print(p1.__class__)
p1.moveBy(1, 1)
p2.moveBy(2, 3)
p3.moveBy(3, 6)

p1.display()
p2.display()
p3.display()


