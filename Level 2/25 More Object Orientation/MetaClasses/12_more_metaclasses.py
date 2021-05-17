# compare two ways of creating classes - roughly equivalent

def use_conventional_class():
    print("\nuse conventional class")
    print("======================")
    class Car:
        def __init__(self, make, model, year, color = 'Black'):
            self.make = make
            self.model = model
            self.year = year
            self.color = color
    
        def display(self):
            return "{} {} {} {}".format(self.color, self.year, self.make, self.model)

    new_car = Car(make='Toyota', model='Prius', year=2005, color='Green')
    old_car = Car(make='Ford', model='Prefect', year=1979)
    print(new_car.display())
    print(old_car.display())

def use_class_factory():
    print("\nuse class factory")
    print("=================")
    
    class MyClassFactory(type):
        def __call__(self, **kwargs):
            # create the object
            obj = type.__call__(self)
            # set default value for color
            setattr(obj, 'color', 'Black')
            # set attributes on the new object
            for name, value in list(kwargs.items()):
                setattr(obj, name, value)
            # return the new object.
            return obj
    
    class Car(metaclass=MyClassFactory):
        def display(self):
            return " ".join(str(getattr(self, attr)) for attr in self.__dict__)
    
    new_car = Car(make='Toyota', model='Prius', year=2005, color='Green')
    old_car = Car(make='Ford', model='Prefect', year=1979)
    print(new_car.display())
    print(old_car.display())

use_conventional_class()
use_class_factory()
