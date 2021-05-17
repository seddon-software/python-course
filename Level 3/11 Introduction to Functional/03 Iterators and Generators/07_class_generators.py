############################################################
#
#    generators
#
############################################################

# generators are a shortcut to building iterators
# class methods can be generators

# the class is not iterable in sense that 
#    the class doesn't define __iter__() and __next__()
# but any method that contains yield 
#    will be converted to an iterator internally

import dis

class Fibonacci:
    def __init__(self):
        self.x,self.y = 0,1
        
    def myGeneratorFunction(self):
        while self.x < 100:
            yield self.x     # suspends execution and returns
            self.x, self.y = self.y, self.x + self.y
        return               # no more yields left

f = Fibonacci()              # create object
g = f.myGeneratorFunction()  # call generator function to create an iterable


for n in g:                  # invoke the iterable
    print(n, end=" ")


