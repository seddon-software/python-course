class Point:
    def __init__(self, x0, y0, name):
        self.x = x0
        self.y = y0
        self.name = name
    
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def display(self):
        print(f"Point {self.name} is at [{self.x},{self.y}]")
