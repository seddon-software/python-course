############################################################
#
#    Adapter
#
############################################################

from abc import ABCMeta, abstractmethod


# this is the new interface we want to use
class ITarget(object, metaclass=ABCMeta):
    @abstractmethod
    def f1(self,x): pass
    
    @abstractmethod 
    def f2(self,x): pass


# this is a new class conforming to the new interface
class Target(ITarget):
    def f1(self,x): print(x, x*2, x*4)
    def f2(self,x): print(x, x/2, x/4)



# this is the old class which uses the wrong interface
class OurClass(object):
    def g1(self,x): print(x, end=' ')
    def g2(self,x): print(x*2, end=' ')
    def g3(self,x): print(x*4, end=' ')
    def g4(self,x): print(x/2, end=' ')
    def g5(self,x): print(x/4, end=' ')
    def g6(self):  print()


# this is the Adapter class
class Adapter(ITarget, OurClass):
    def f1(self,x): 
        self.g1(x)
        self.g2(x)
        self.g3(x)
        self.g6()
        
    def f2(self,x): 
        self.g1(x)
        self.g4(x)
        self.g5(x)
        self.g6()


##### Test

def test(target):
    target.f1(32)
    target.f2(20)


t1 = Target()
t2 = Target()
adapter1 = Adapter()
adapter2 = Adapter()

# check we can use target and adapter objects
test(t1)
test(t2)
test(adapter1)
test(adapter2)

