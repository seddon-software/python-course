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
    
def Check(obj):
    if isinstance(obj, object): print(obj.name + ": object")
    if isinstance(obj, Person): print(obj.name + ": Person")
    if isinstance(obj, Employee): print(obj.name + ": Employee")
    if isinstance(obj, SalesPerson): print(obj.name + ": SalesPerson")
    
    
p = Person("Anne")
e = Employee("Beth", 7468)
s = SalesPerson("Carol", 4712, "NE")
if type(s) is Person: print("s is a Person")
if type(s) is Employee: print("s is a Employee")
if type(s) is SalesPerson: print("s is a SalesPerson")

Check(p)
Check(e)
Check(s)

1

