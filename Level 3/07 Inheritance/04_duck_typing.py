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