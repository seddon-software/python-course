from abc import ABC, abstractmethod

# define an interface
class IShape(ABC):
    @abstractmethod
    def draw(self): pass
    @abstractmethod
    def hide(self): pass
    @abstractmethod
    def show(self): pass

# define default implementations in abstract class
class Shape(IShape):
    def draw(self): print("default impl of draw")
    
# define concrete implementations
class Triangle(Shape):
    def draw(self): 
        Shape.draw(self)
    def hide(self): print("Triangle hide")
    def show(self): print("Triangle show")
    
class Rectangle(Shape):
    def draw(self): print("Rectangle draw")
    def hide(self): print("Rectangle hide")
    def show(self): print("Rectangle show")

class Ellipse(Shape):
    def draw(self): print("Ellipse draw")
    def hide(self): print("Ellipse hide")
    def show(self): print("Ellipse show")

def drawAnyShape(s):
    s.draw()

t = Triangle()
r = Rectangle()
e = Ellipse()
drawAnyShape(t)
drawAnyShape(r)
drawAnyShape(e)

try:
    s = Shape() # try to instantiate an abstract class
except Exception as e:
    print(e)
