############################################################
#
#    decorators
#
############################################################


# decorators can be classes (but must be callable)

class MyClass(object):
    def __init__(self, fn):
        print("class decorator CTOR called")
        self.fn = fn        # save function pointer or later use
    
    # must be callable
    def __call__(self):
        print("decorator called")
        self.fn()


# class decorators create an anonymous object of MyObject
# and then call the CTOR with f as a parameter
@MyClass
def f(): 
    print("f()")



# since f is decorated, the call f()
# is replaced with a call to anon.__call__()
# where anon is the anonymous object created above
f()     

# undecorated form is:
# MyClass(f).__call__()


1
