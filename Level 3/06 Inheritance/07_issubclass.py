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
    
def Check(A, B):
    if issubclass(A, B): 
        print(str(A) + " is subclass of " + str(B))
    else:
        print(str(A) + " is NOT subclass of " + str(B))
    
    

Check(Person, Employee)
Check(Person, SalesPerson)
Check(Employee, Person)
Check(Employee, SalesPerson)
Check(SalesPerson, Person)
Check(SalesPerson, Employee)

1

