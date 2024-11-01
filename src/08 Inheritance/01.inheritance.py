'''  
  In Python, when we use inheritance, derived classes inherit all the methods and attributes from
  their base class.  A derived class declares it's base class in brackets:
  
            class Bus(Vehicle):
            class Car(Vehicle):
            class Van(Vehicle):
  
  
  Methods in the base class (Vehicle) usually have parameters, but I've left them out in 
  this example to keep things simple.  Bus, Car and Van all inherit the methods:
            start(), refuel() and stop().

  The idea behind inheritance is code reuse.  This in turn implies that classes in an inheritance
  hierarchy must be closely related.  Since all derived classes inherit methods and attributes from their 
  base class, they can always substitute for base class objects in functions.  This is called:
            THE SUBSTITUTION RULE
 
  Here Bus, Car and Van objects can SUBSTITUTE for Vehicle objects.  In the function:
            def refuelAnyVehicle(vehicle): ... 
 
  The reference to a vehicle in this function indicates that a Bus, Car or Van object might be passed 
  to the function instead of a vehicle.  This in turn implies that the function can only call methods 
  defined in the Vehicle class; this is fine because all derived classes will inherit these methods.
 
  Derived classes are free to add additional methods and attributes.  It is important to realize that 
  derived classes always contain at least he same number of methods and attributes as their base class 
  and hence the substitution rule is one way; a derived object can substitute for a base class object, 
  but because the base class might be missing some of the derived class's methods and attributes, a base 
  class object can't substitute for a derived object.
 
  Note that derived classes can provide additional versions of base class methods if they need different
  behaviour from the base class; the Bus class provides a second version of the refuel method.  This means
  the Bus class now has 4 methods:
            Vehicle.start()
            Vehicle.stop()
            Vehicle.refuel()
            Bus.refuel()
'''

# this class acts as a placeholder for methods shared with derived classes.  
# we do not expect to create objects of this class and therefore it is called an ABSTRACT class
class Vehicle:
    def start(self): print("vehicle starting ...")
    def stop(self): print("vehicle stopping ...")
    def refuel(self): print("vehicle refueling ...")

class Bus(Vehicle): # inherits 3 methods from Vehicle, plus one it defines itself
    def refuel(self): print("bus refueling ...")

class Car(Vehicle): # inherits 3 methods from Vehicle, plus one it defines itself
    def refuel(self): print("car refueling ...")

class Van(Vehicle): # inherits 3 methods from Vehicle, plus one it defines itself
    def refuel(self): print("van refueling ...")

# code reuse:  this function can be used by any class derived from Vehicle
def refuelAnyVehicle(vehicle):
    # note this will call the refuel method in the appropriate derived class
    vehicle.refuel();

def main():
    bus = Bus()
    bus.start()
    bus.refuel()
    bus.stop()

    car = Car()
    car.start()
    car.refuel()
    car.stop()
    
    van = Van()
    van.start()
    van.refuel()
    van.stop()

    # now use the SUBSTITUTION RULE to refuel all 3 vehicles
    refuelAnyVehicle(bus);
    refuelAnyVehicle(car);
    refuelAnyVehicle(van);

    # note the following is possible, but doesn't make sense, because the Vehicle class is abstract:
    vehicle = Vehicle()
    vehicle.start();
    vehicle.refuel();
    vehicle.stop();

main()
