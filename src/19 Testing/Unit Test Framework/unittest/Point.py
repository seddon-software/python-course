class Point:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0

    def get_distance(self):
        return (self.x ** 2 + self.y **2) **0.5

    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def display(self):
        return str(self.x) + "," + str(self.y)
        
    
