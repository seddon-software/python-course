'''
Calling Constructors
====================

Here is a typical example of an inheritance hierarchy.  

            Person
               ▲
               │
           Employee
               ▲
               │
          SalesPerson

Note how each class calls constructors in it's immediate base class.  Furthermore, each object has a dictionary 
containing all attributes, even those defined in the base classes.
'''

class Person(object):
    def __init__(self, name):
        self.name = name
        
class Employee(Person):
    def __init__(self, name, id):
        Person.__init__(self, name)
        self.id = id
    
class SalesPerson(Employee):
    def __init__(self, name, id, region):
        Employee.__init__(self, name, id)
        self.region = region
    

# create objects of each class in hierarchy
p = Person("Anne")
e = Employee("Beth", 7468)
s = SalesPerson("Carol", 4712, "NE")

# examine object dictionaries
print(p.__dict__)
print(e.__dict__)
print(s.__dict__)



