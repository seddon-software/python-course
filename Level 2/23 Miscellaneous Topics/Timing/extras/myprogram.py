import cProfile

class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def getDetails(self):
        return self.name + "," + str(self.age) + "," + self.address

class PersonSlots(object):
    __slots__ = ['name', 'age', 'address']
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def getDetails(self):
        return self.name + "," + str(self.age) + "," + self.address

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

count = 0

def f1():
    global count
    for i in xrange(10000):
        count = count + i

def f2():
    global count
    for i in xrange(20000):
        count = count + i

def f3():
    global count
    for i in xrange(30000):
        count = count + i

def f4():
    global count
    for i in xrange(40000):
        count = count + i


def foo():
    for i in range(10):
        f1()
        f2()
        f3()
        f4()
    
