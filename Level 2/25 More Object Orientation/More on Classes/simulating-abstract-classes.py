from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def method1(self): pass
    @abstractmethod
    def method2(self): pass
    def method3(self): 
        print("This method is implemented")

class MyClassA(MyAbstractClass): 
    # class should implement method1 and method2
    def method1(self):
        print("method1")

class MyClassB(MyAbstractClass): 
    # class does implement method1 and method2
    def method1(self):
        print("method1")
    def method2(self):
        print("method1")

# call methods
try:
    a = MyClassA()
    a.method1()
    a.method2()
    a.method3()
except Exception as e:
    print(e)
    
# this is OK
b = MyClassB()
b.method1()
b.method2()
b.method3()
