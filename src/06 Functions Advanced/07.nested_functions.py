'''
Functions can call other function.  This is illustrated below with the "powers" function.

Furthermore functions can be nested.  The function "powers2" shows how nesting works.  Note how
the parameter passed to "powers2" can be seen by the nested functions.  This means you don't have
to pass the parameter to the nested functions explicitly, thereby simplifying the code.  

So compare the global functions with the nested ones.  For example the global "square":
            def square(n):
                return n**2

takes a parameter "n", but the nested version doesn't:
            def square():
                return n**2

Nested functions can see their environment (defined by the encapsulating function), in this case the 
parameter "n".  This feature is called "closure".
'''

def square(n):
    return n**2

def cube(n):
    return n**3

def quad(n):
    return n**4

def powers(n):
    print(f"{n} squared = {square(n)}")
    print(f"{n} cubed = {cube(n)}")
    print(f"{n} to 4th power = {quad(n)}")

def powers2(n):
    def square():
        return n**2

    def cube():
        return n**3

    def quad():
        return n**4
    print(f"{n} squared = {square()}")
    print(f"{n} cubed = {cube()}")
    print(f"{n} to 4th power = {quad()}")

powers(5)
powers2(10)

