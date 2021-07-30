class Driver:
    def __init__(self, name):
        self.name = name
    
    def ChangeCar(self, car):
        self.car = car
    
    def getDetails(self):
        return self.name + " drives " + self.car.getMake()

class Car:
    def __init__(self, make):
        self.make = make
    
    def getMake(self):
        return self.make

alonso = Driver("Fernando Alonso")
hamilton = Driver("Lewis Hamilton")
maclaren1 = Car("Maclaren-Mercedes-1")
maclaren2 = Car("Maclaren-Mercedes-2")
renault1 = Car("Renault-1")
renault2 = Car("Renault-2")

alonso.ChangeCar(maclaren1)
hamilton.ChangeCar(maclaren2)
print(alonso.getDetails())
print(hamilton.getDetails())

alonso.ChangeCar(renault1)
hamilton.ChangeCar(maclaren1)
print(alonso.getDetails())
print(hamilton.getDetails())

1