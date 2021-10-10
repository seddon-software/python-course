import inspect

class Point:
    def __init__(self): pass
    def move(self): pass
    def display(self): pass
    
print("-----------------")
print(inspect.getsource(Point))

