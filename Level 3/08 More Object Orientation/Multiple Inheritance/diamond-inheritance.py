class Item(object):
    def __init__(self, price):
        self.price = price
    def getPrice(self):
        return self.price
    
class TaxableItem(Item):
    def __init__(self, name, price):
        Item.__init__(self, price * 0.95) # 5% discount
        self.name = name
        
class Car(Item):
    def __init__(self, make, price):
        Item.__init__(self, price - 1000) # 1000 discount
        self.make = make

# create CompanyCar in 4 possible ways:
#    inherit from (TaxableItem, Car) or (Car, TaxableItem)
#    call CTORs TaxableItem first or Car first
#    gives 4 possible combinations (=> different results)      
class CompanyCar1(TaxableItem, Car):
    def __init__(self, name, make, price):
        TaxableItem.__init__(self, name, price)
        Car.__init__(self, make, price)
    
class CompanyCar2(TaxableItem, Car):
    def __init__(self, name, make, price):
        Car.__init__(self, make, price)
        TaxableItem.__init__(self, name, price)
    
class CompanyCar3(Car, TaxableItem):
    def __init__(self, name, make, price):
        Car.__init__(self, make, price)
        TaxableItem.__init__(self, name, price)
    
class CompanyCar4(Car, TaxableItem):
    def __init__(self, name, make, price):
        TaxableItem.__init__(self, name, price)
        Car.__init__(self, make, price)
    

myCar1 = CompanyCar1("chris", "bmw", 32000)
myCar2 = CompanyCar2("chris", "bmw", 32000)
myCar3 = CompanyCar3("chris", "bmw", 32000)
myCar4 = CompanyCar4("chris", "bmw", 32000)

print(myCar1.getPrice())
print(myCar2.getPrice())
print(myCar3.getPrice())
print(myCar4.getPrice())

1