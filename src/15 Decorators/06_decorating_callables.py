'''
Decorating Callables
====================

Decorators can be classes, but the class must be callable.  This means the class must override the () operator
with the dunder method
            __call__()

Decorators are designed to be functions that are inserted in the normal call logic.  Thus if a function "f" is
decorated with "g" then calls such as
            f()

will be translated to
            g(f)()

Also, note that when we are dealing with classes for a given object o then
            o()
is the same as
            o.__call__()

Now we make __call__ a decorator.

When we write:
            @MyClass
            def f(): 
the function "f" is decorated.  Now the call
            f()
gets translated in to:
            MyClass(f)()
which creates a temporary object and the constructor stores f in its dictionary (self.fn).  The additonal brackets
are a call on this temporary object:
            temp()
or
            temp.__call__()

The body of this function is:
            print("extra decorating code")
            self.fn() 
and because self.fn was assigned to f in the constructor this is the same as
            print("extra decorating code")
            f()
Thus we still ultimately call "f", but insert extra code (in this case, the print statement) before the call.
Obviously this extra code can be a complex as you like and hence it "decorates" the call to "f".
'''

# decorators can be classes (but must be callable)
class MyClass(object):
    def __init__(self, fn):
        print("object of MyClass created, CTOR called")
        self.fn = fn        # save function pointer or later use
    
    # must be callable
    def __call__(self):
        print("extra decorating code")
        self.fn()


# class decorators create a temporary object of type MyObject
# and then call the CTOR with f as a parameter
@MyClass
def f(): 
    print("f() called")



# since f is decorated, the call f()
# is replaced with a call to temp.__call__()
# where temp is the temporary object discussed above
f()     

# undecorated form is:
# MyClass(f).__call__()



