'''
f-strings are used extensively in modern Python.  They allow customisation of formating.  All classes
should probably provide the methods:
        __str__     returns a string to print the object (intended for production code)
        __repr__    returns a string to print the object (intended for debugging)

These methods can be invoked by the special f-string formating symbols
        !s          invokes __str__
        !r          invokes __repr__
If you try different letter then __format__ will be called and you can define you own customized formatter.
'''

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"__str__: {self.x, self.y, self.z}"

    def __repr__(self):
        return f"__repr__:{self.x, self.y, self.z}"

    def __format__(self, format_spec: str):
        if not format_spec or format_spec == "s":
            return str(self)
        
        if format_spec == "r":
            return f"r:{self.x, self.y, self.z}"
        if format_spec == "w":
            return f"w:{self.x, self.y, self.z}"
p = Point(1, 2, 3)
print(f"{p!s}")     # calls __str__
print(f"{p!r}")     # calls __repl__
print(f"{p:s}")     # calls __format__
print(f"{p:r}")     # calls __format__
print(f"{p:w}")     # calls __format__


