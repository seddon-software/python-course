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
c1 + c2

# take a look at other special (dunder) methods:
import webbrowser
url = "https://holycoders.com/python-dunder-special-methods/"
webbrowser.open(url)
