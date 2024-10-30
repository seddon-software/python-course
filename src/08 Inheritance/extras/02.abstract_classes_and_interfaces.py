'''
We can take a more formal approach to abstract classes using the ABC (Abstract Base Class) module.  This module provides the 
infrastructure for defining abstract base classes (ABCs) in Python, as outlined in PEP 3119.

We use decorators to define abstract methods that must be defined in the concrete derived classes.  Note that an interface class 
is made up entirely of abstract methods.  It is a common convention to prepend class names with "I" to indicate an interface class.
Note how the Shape class is used to define a default implementation for the draw method, but because it doesn't define the 
other methods specified in the interface IShape (hide() and show()), the Shape class is itself abstract and can't be instantiated 
(see the end of the example).

             IShape
                ^
                |
                |
              Shape
                ^
               /|\
              / | \
             /  | \
            /   |  \
           /    |   \
          /     |    \
         /      |     \
        /       |      \
  Triangle Rectangle Ellipse      
'''

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
        print("Triangle rest of draw")
    def hide(self): print("Triangle hide")
    def show(self): print("Triangle show")
    
class Rectangle(Shape):
    def draw(self): 
        Shape.draw(self)
        print("Rectangle rest of draw")
    def hide(self): print("Rectangle hide")
    def show(self): print("Rectangle show")

class Ellipse(Shape):
    def draw(self): print("Ellipse draw")
    def hide(self): print("Ellipse hide")
    def show(self): print("Ellipse show")

def drawAnyShape(s):  # Shape, Triangle, Rectangle or Ellipse
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
