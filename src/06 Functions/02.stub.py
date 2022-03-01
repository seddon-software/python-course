'''
Empty (stub) Functions
======================

Languages like Java and C have a way of defining an empty function.  For example, in C, we can write:
        void myStub(int x, int y)
        {}

The body of this function is empty.  Empty functions are used during development for testing; code is added
to these empty functions as the project develops.  In Python, we can't use {} for empty functions since {} is 
used for dictionaries.

This example shows how the "pass" instruction is used to create an enmpty function object.
'''


def myStub(x, y):
    pass



myStub(5,6)
myStub(1,10)
myStub(0,7)




