# This example shows how to create classes from Python's fundamental
# factory method: type
# 
# To create the class, the metaclass is called with the following arguments:
#
#    type(name, bases, dict)
#
#    'name': The name of the class
#    'bases': A tuple of the base classes of the class
#    'dict': A dictionary of the attributes of the class



############################################################
# conventional class definition

class TestA:
    def __init__(self, x):
        self.x = x

    def printX(self):
        print(self.x)

############################################################
# alternative way to define a class

def __init__(self, x):
    self.x = x

def printX(self):
    print(self.x)

className = 'TestB'
bases = (object,)
dictionary = {
              '__init__': __init__, 
              'printX'  : printX
             }
TestB = type(className, bases, dictionary)


############################################################
# main

ta = TestA(10)
ta.printX()

tb = TestB(10)
tb.printX()




1