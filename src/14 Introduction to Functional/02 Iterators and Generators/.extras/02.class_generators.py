import os; os.system("clear")
'''
Class Generators
================

As we have seen, generators are a shortcut to building iterators.  Sometimes we want to make a method of a
class into a generator; any method that contains "yield" will be converted to an iterator internally.
'''

class Fibonacci:
    def __init__(self):
        self.x,self.y = 0,1
        
    def myGeneratorFunction(self):
        while self.x < 100:
            yield self.x     # suspends execution and returns
            self.x, self.y = self.y, self.x + self.y
        return               # no more yields left

f = Fibonacci()              # create object
g = f.myGeneratorFunction()  # call generator function to create an iterator


for n in g:                  # loop with the iterator
    print(n, end=" ")


