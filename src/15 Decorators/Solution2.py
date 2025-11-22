'''
Decorators with Attributes
==========================

You can have all sorts of decorators.  In this exmple we look at decorators with method attributes.
This time we have two functions
            circle() 
            square()

that are decorated with method instances of MyClass (@red.div and @blue.span).

Now a call to circle() gets translated to:
            red.div(cicle)()

and red.div is a simple decorator that returns "inner()":
            MyClass.inner() with closure on self.color = "red" and fn = circle
and hence executes
            print(f'<div class="{self.color}">{fn()}</div>')
which translates to:
            print(f'<div class="red">circle()</div>')
and prints
            <div class="red">circle()</div>
'''


class MyClass(object):
    def __init__(self, color):
        self.color = color

    def div(self, fn):
        def inner():
            print(f'<div class="{self.color}">{fn()}</div>')
        return inner

    def span(self, fn):
        def inner():
            print(f'<span class="{self.color}">{fn()}</span>')
        return inner

        
red = MyClass("red")
blue = MyClass("blue")

@red.div
def circle():
    return "This is a circle"

@blue.span
def square():
    return "This is a square"



circle()    # red.div(circle)()
square()    # blue.span(square)()


