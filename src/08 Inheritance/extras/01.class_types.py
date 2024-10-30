'''
Normally because of polymorphism, it is not neccessary to know the exact class of an object; you can rely on the substitution rule.  
But if you really want to to know you can resort to using the "type" ibuilt-in.  Alternatively you can check if an object can
substitute for a polymorhic object using the "isinstance" built-in.

Furthermore you can use "issubclass" to check where a class resides in the inheritance hierachy.  Note a class is always considered
a subclass of itself.
'''

class Person:
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
    
p = Person("Anne")
e = Employee("Beth", 7468)
s = SalesPerson("Carol", 4712, "NE")

def doSomething(p):
    # check for exact type
    if type(p) is Person: print(f"{p.name} is of type Person")
    if type(p) is Employee: print(f"{p.name} is of type Employee")
    if type(p) is SalesPerson: print(f"{p.name} is of type SalesPerson")

    # check for ISA relationships
    if isinstance(p, object): print(f"{p.name} IS A object")
    if isinstance(p, Person): print(f"{p.name} IS A Person")
    if isinstance(p, Employee): print(f"{p.name} IS A Employee")
    if isinstance(p, SalesPerson): print(f"{p.name} IS A SalesPerson")

# examine ISA and type
doSomething(p)
doSomething(e)
doSomething(s)

def Check(A, B):
    if issubclass(A, B): 
        print(f"{A.__name__} is subclass of {B.__name__}")
    else:
        print(f"{A.__name__} is NOT subclass of {B.__name__}")
    
# check class relationships
Check(Person, Person)
Check(Person, Employee)
Check(Person, SalesPerson)
Check(Employee, Person)
Check(Employee, SalesPerson)
Check(SalesPerson, Person)
Check(SalesPerson, Employee)




