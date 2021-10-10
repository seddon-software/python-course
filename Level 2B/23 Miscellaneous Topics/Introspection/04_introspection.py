############################################################
#
#    introspection
#
############################################################

class Point:
    """
    This is an example for introspection
    """
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
    
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def display(self):
        print("Point is at: ", self.x, ",", self.y)

# use object
p = Point(3,4)
p.moveBy(1,1)
p.display()

# investigate object
print("methods and attributes:", dir(p))
methodList = [method for method in dir(p) if callable(getattr(p, method))]
print("methods:", methodList)
print("attributes: ", p.__dict__)
print("class:", p.__class__)
print("doc string:", p.__class__.__doc__)
