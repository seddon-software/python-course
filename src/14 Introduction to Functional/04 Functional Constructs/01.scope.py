'''
There are 4 different scopes in Python: LEGB

The letters in the acronym LEGB stand for Local, Enclosing, Global, and Built-in scopes. 
This summarizes not only the Python scope levels but also the sequence of steps that Python follows when 
resolving names in a program.

Try commenting out "sum" in various parts of this program.

n.b. the global variable 'sum' hides the built-in sum function (this is intentional)
'''
# the builtin function 'sum' is of built-in scope

sum = 99        # global scope

def outer():
    sum = 88    # enclosing scope
    def inner():
        sum = 77  # local scope
        print(sum)
    inner()

outer()
