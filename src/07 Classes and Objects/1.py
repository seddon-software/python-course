class Point:
    # CTOR
    def __init__(self, name, x0, y0):
        self.__dict__['x'] = x0
        self.y = y0
        self.name = name
    def moveBy(self, dx, dy):
        self.x = self.x + dx
        self.y += dy
    def display(self):
        print(f"Point {self.name} is at [{self.x},{self.y}]")

# create some objects
print(Point.__dict__)
p1 = Point('point-p1', 100, 300)
p2 = Point('point-p2', 110, 320)
p3 = Point('point-p3', 120, 340)
p1.moveBy(1, 10)
p2.moveBy(2, 20)
p3.moveBy(3, 30)
p1.display()
p2.display()
p3.display()
