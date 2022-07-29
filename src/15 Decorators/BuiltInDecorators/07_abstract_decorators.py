'''
Abstract Decorator
==================

In object oriented theory a class can be abstract in the sence it can't be instantiated.  This is usually when a
class acts as the base class of an inheritance hierarchy.  In this example we define classes that can be 
instantiated:
            Circle
            Square
            Rhombus

that inherit from the class Shape with the resultant inheritance hierarchy:

                           Shape
                             |
                             |
                   ┌─────────┐───────┐
                   │         │       │
                 Circle   Square  Rhombus


However Shape is abstract and the abstractmethod decorator and abstractproperty decorator ensures that Shape 
objects cannot be created.  All derived classes mist provide concreate implementations of these methods and 
attributes or they too will be abstract. 

Note: the abstract methods in Shape do not contain any code (just "pass").
'''

from abc import ABCMeta, abstractmethod, abstractproperty

# define inheritance hierachy
class Shape(object, metaclass=ABCMeta):
    @abstractmethod
    def display(self): pass
	
    @abstractproperty
    def name(self):	pass

class Circle(Shape):
    def __init__(self, name):
        self.theName = name
		
    def display(self):
        print(f"Circle: {self.name}")
		
    @property
    def name(self):
    	return self.theName

class Square(Shape):
    def __init__(self, name):
        self.theName = name
		
    def display(self):
        print(f"Square: {self.name}")
		
    @property
    def name(self):
    	return self.theName

class Rhombus(Shape):
    def __init__(self, name):
        self.theName = name
		
    def display(self):
        print(f"Rhombus: {self.name}")
		
    @property
    def name(self):
    	return self.theName
    	
c = Circle("my-circle")
s = Circle("my-square")
r = Circle("my-rhombus")
print(f"name property: {c.name}") 
print(f"name property: {s.name}") 
print(f"name property: {r.name}") 
c.display()
s.display()
r.display()

# try to instantiate a Shape object
try:
	 s = Shape()
except TypeError as e:
	print(f"{e}")

