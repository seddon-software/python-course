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
    

p = Person("Anne")
e = Employee("Beth", 7468)
s = SalesPerson("Carol", 4712, "NE")
print(p.__dict__)
print(e.__dict__)
print(s.__dict__)



1