import os; os.system("clear")
'''
In the inheritance hierarchy below:

            Person
                ^
                |
                |
            Employee
                ^
                |
                |
            SalesPerson

the base class defines 3 methods:
            Eat() 
            Drink() 
            Sleep() 

The derived classes provide their own versions of these methods (each with a different implementation).  This means there
are several versions of the base class methods.  Such methods are called polymorpic methods because there are many (poly) 
forms (morphic) of the methods.  Note that the derived classes inherit the base class methods, but choose to override them.

We can now define a method that takes as a parameter a (polymorphic) object of any of the classes in the hierarchy:
            NightOut(p)

The parameter p can be either a Person, Employee or SalesPerson.  This works because all the classes implement the same
polymorphic methods (albeit differently).  We say
            p IS A Person, Employee or SalesPerson
by the substitution rule.  When the function is called with different objects, the same code behaves differently (but
appropriately) for each object.  This allows such methods to vary their behaviour in a polymorphic way.
'''

class Person:
    def Eat(self): print("MacDonalds")
    def Drink(self): print("Coke")
    def Sleep(self): print("ZZZZZZZZ")
    
class Employee(Person):
    def Eat(self): print("Nandos")
    def Drink(self): print("Wine")
    
class SalesPerson(Employee):
    def Eat(self): print("Fat Duck")
    def Drink(self): print("Champagne")
    # many forms => poly morphism

# this method takes a polymorhic object as a parameter
def NightOut(p):  # p ISA Person, Employee or SalesPerson (Substitution rule)
    p.Drink()
    p.Drink()
    p.Eat()
    p.Drink()
    p.Sleep()
    
# create objects for each class in the hierarchy
p = Person()
e = Employee()
s = SalesPerson()

# each object behaves differently on a night out
NightOut(p)
NightOut(e)
NightOut(s)
