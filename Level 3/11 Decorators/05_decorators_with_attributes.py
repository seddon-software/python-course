############################################################
#
#    decorators
#
############################################################



class MyClass(object):
    def __init__(self, color):
        self.color = color

    def div(self, fn):
        # print(fn)
        def inner():
            print('<div class="{0}">{1}</div>'.format(self.color, fn()))
        return inner

    def span(self, fn):
        # print(fn)
        def inner():
            print('<span class="{0}">{1}</span>'.format(self.color, fn()))
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


1
