class Point:
    # method
    # CTOR
    # self points to object dict
    # Point points to class (shared) dict
    def getCount():     
        return Point.count
    def __init__(self, name, x0=0, y0=0):   # self points at the dict
        Point.count += 1
        self.x = x0
        self.y = y0
        self.name = name
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    def display(self):
        print(f"{self.name}: {self.x},{self.y}")
    count = 0



##### create instances (objects) of thee class

print(Point.getCount())
p1 = Point("point-p1", 100, 200)
p1.count = p1.count   # RHS => all dictionaries searched
                      # LHS => only the object dict is used
print(p1.__dict__)
p2 = Point("point-p2", 110, 210)
p3 = Point("point-p3")
print(Point.getCount())
print(p1.count)
print(p1.__dict__)
p1.moveBy(1, 1)
p2.moveBy(1, 1)
p3.moveBy(1, 1)
p1.display()
p2.display()
p3.display()
print()
