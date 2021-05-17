class Taxable:
    def __init__(self, name, price):
        self.price = price
        self.name = name
        
class Car():
    def __init__(self, make):
        self.make = make
    
class CompanyCar(Taxable, Car):
    def __init__(self, name, make, price):
        Taxable.__init__(self, name, price)
        Car.__init__(self, make)
    

myCar = CompanyCar("chris", "bmw", 32000)


1