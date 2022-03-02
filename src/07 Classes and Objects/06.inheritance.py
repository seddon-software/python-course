'''
Working with Inheritance
========================

When we have an inheritance hierachy, we may overload a dunder method in more than one class.  Then we may
ask: "which dunder method gets called"?

If you run the code below you will see that the rule is: call the method for the class of the left hand operand.
Since __add__() is only overloaded in classes A and C, when A or B objects are involved A.__add__() is used. 
However, if a C object is the left operand then C._add__() is invoked.
'''

class A:
    def __add__(self, rhs):
        print("A.__add__() called")

class B(A):
    # this class inherits __add__ from its super class
    pass

class C(B):
    # this class defines a polymorphic __add__ method
    def __add__(self, rhs):     # dunder method
        print("C.__add__() called")

a1 = A()
a2 = A()
b1 = B()
b2 = B()
c1 = C()
c2 = C()

a1 + a2
b1 + b2
b1 + c2
c1 + b2
c1 + c2

# take a look at other special (dunder) methods:
import webbrowser
url = "https://holycoders.com/python-dunder-special-methods/"
webbrowser.open(url)
