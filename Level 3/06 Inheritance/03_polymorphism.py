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

1