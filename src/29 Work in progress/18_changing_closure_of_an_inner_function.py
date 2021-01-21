import types
import functools

# how to change the closure on an inner function
# for the purposes of testing inner functions

def copy_func(oldFunction, newClosure):
    """Based on http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)"""
    newFunction = types.FunctionType(oldFunction.__code__, 
                           oldFunction.__globals__, 
                           name=oldFunction.__name__,
                           argdefs=oldFunction.__defaults__,
                           closure=newClosure)
    newFunction = functools.update_wrapper(newFunction, oldFunction)
    newFunction.__kwdefaults__ = oldFunction.__kwdefaults__
    return newFunction

def test(closure, expected):

    def decorator(fn):
        # create a closure with the new values passed in 'closure'
        def create_closure():
            def make_cell(value):
                fn = (lambda x: lambda: x)(value)
                return fn.__closure__
            cells = []
            for i,c in enumerate(closure):
                cells.append(make_cell(closure[i])[0])
            return cells
        
        cells = create_closure()
        
        # create a duplicate of the inner function, but with a different closure
        duplicate_function = copy_func(fn, tuple(cells))

        # perform test to see if expected result matches actual result
        actual = duplicate_function()
        print(expected == actual)
        
        # return original function, so original values are used
        return fn
    
    return decorator

def f1():
    x = [11, 20, 30, 40]
    y = (5, 6, 7)
    @test(closure=[[10, 20, 30, 40],(1,1,1)], expected=103)
    def f2():
        return sum(x) + sum(y)
    return f2()

print(f1())
