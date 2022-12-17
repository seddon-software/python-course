class MyClass(object):  # new style class
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # called if attribute can't be found by lookup
    def __getattr__(self, name):
        print("__getattr__")
        self.__dict__[name] = None # used to avoid recursion
        return self.__dict__[name]
    
    # always called if attribute is read
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)    
    
    # always called if attribute is written
    def __setattr__(self, name, value):
        print("__setattr__")
        self.__dict__[name] = value
            
    def __str__(self):
        return str(self.__dict__)

# create an object
obj = MyClass(22, 66)

# examine standard attributes
print(obj.x)
print(obj.y)

# examine undefined attributes
print(obj.aaa)

# set new attributes
obj.bbb = 5
print(obj.bbb)

# dictionary access bypasses all hooks (except __getattribute__(obj,__dict__))
obj.__dict__['ccc'] = 77

# display all attributes defined so far
print(obj)

1