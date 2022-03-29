class Point:
    count = 0
    def getCount():
        return Point.count

    def __init__(self, x0=0, y0=0):
        Point.count += 1
        self.x = x0
        self.y = y0

    def moveBy(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def display(self):
        print(f"Point is at [{self.x},{self.y}]")



# create objects
q = Point()
p1 = Point(100, 250)        # __init__() called automatically
p2 = Point(110, 260)
p3 = Point(120, 270)
print(Point.getCount())
# print(p1.count)             # searches object dict, then class dict etc
# p1.count = 99               # adds entry to object dict

p1.count = p1.count
print(p1.__dict__)
p1.moveBy(10, 20)
p2.moveBy(11, 21)
p3.moveBy(12, 22)
p1.display()
p2.display()
p3.display()


# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)
# print(p1.__class__)
# print(p2.__class__)
# print(p3.__class__)
