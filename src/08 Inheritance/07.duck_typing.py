'''
One of the problems with polymorphism in Python is that an object that is not in the inheritance hierarchy (Horse) can
be passed to a polymorhic method provided it implements the same set of polymorphic methods even though it doesn't make
sense.  This is called duck typing:
            If it walks like a duck, quacks like a duck then it is a duck

Although undesirable, it is difficult to prevent objects behaving in this way (but see the next example).
'''

class Person:
    def Eat(self): pass
    def Drink(self): pass
    def Sleep(self): pass
    
class Employee(Person):
    def Eat(self): pass
    def Drink(self): pass
    def Sleep(self): pass
    
class SalesPerson(Employee):
    def Eat(self): pass
    def Drink(self): pass
    def Sleep(self): pass
    
class Horse:
    def Eat(self): pass
    def Drink(self): pass
    def Sleep(self): pass
    
def NightOut(p):
    p.Drink()
    p.Drink()
    p.Eat()
    p.Drink()
    p.Sleep()
    

p = Person()
e = Employee()
s = SalesPerson()

NightOut(p)
NightOut(e)
NightOut(s)
h = Horse()
NightOut(h)

1
