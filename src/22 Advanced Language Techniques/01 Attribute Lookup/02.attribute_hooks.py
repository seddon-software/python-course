'''
Attribute Hooks
===============

Python allows you to trace access to an object's attributes if you provide any of the following methods: 
            def __getattribute__(self, name):           always called when attempting to read an attribute
            def __getattr__(self, name):                only called when an attribute is undefined
            def __setattr__(self, name, value):         called when writing to an attribute

Recall that you can access an attribute in of two ways, using the dot notation or via the __dict__ as in:
            obj.__dict__['x']
            obj.x

These methods are explored below.

Note that this example is best run on the command line; if you run it in the debugger, the debugger will trigger
spurious attribute accesses and give a false picture of what is going on.
'''

class MyClass:
    # called if attribute can't be found
    def __getattr__(self, name):
        print(f"    __getattr__: {name}")
        return self.__dict__[name]

    # always called if attribute is read
    def __getattribute__(self, name):
        print(f"    __getattribute__: {name}")
        return object.__getattribute__(self, name)

    # always called if attribute is written
    def __setattr__(self, name, value):
        print(f"    __setattr__: {name}={value}")
        self.__dict__[name] = value

    def __str__(self):
        return str(self.__dict__)

##############################################################
# create an object
obj = MyClass()

print("\nset an attribute via dot notation")
input("continue?")
print(">>> obj.x = 99")
obj.x = 99

print("\nset an attribute via dict")
input("continue?")
print(">>> obj.__dict__['x'] = 88")
obj.__dict__['x'] = 88

print("\nread an attribute via dot notation")
input("continue?")
print(">>> obj.x")
obj.x

print("\nread an attribute via dict")
input("continue?")
print(">>> obj.__dict__['x']")
obj.__dict__['x']

print("\ntry to access undefined attribute via dot notation")
input("continue?")
print(">>> obj.unknown")
try:
    obj.unknown
except KeyError as e:
    print(f"KeyError: {e}")

print("\ntry to access undefined attribute via dict")
input("continue?")
print(">>> obj.__dict__['unknown']")
try:
    obj.__dict__['unknown']
except KeyError as e:
    print(f"KeyError: {e}")



