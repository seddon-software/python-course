import os; os.system("clear")
'''
Generators
==========

While iterators work fine in for loops, some people feel they are too complicated.  As a simpler alternative,
Python created generators.  Generators are a special type of iterator.  A generator is defined as any function
that uses the "yield" instruction.

A generator doesn't look like an iterator; where are the __iter__() and __next()__ methods?  The answer is that
the Python interpreter tanslates the generator code into an internal iterator.  Unfortunately you can't see
this iterator, but believe me, it does exist.

The example generator below:
            def powers():
                x = 1
                while(x < 1000):
                    x = x * 2
                    yield x
                    pass        # just to show execution resumes after the yield
                return

gets expanded by the interpreter to something like the following
            class InternalIterator:
                def __init__(self)
                    self.x = 1
                def __iter__(self):
                    return self
                def __next__(self):
                    x = self.x
                    if x >= 1000:
                        raise StopIteration     # indicate end of iteration
                    else:
                        x = x * 2
                        self.x = x
                    return x

Support inside the for loop is now the same as for explicit iterators.  Unfortunately, you can't see the
expanded code in the debugger.

If you step through the code below, recall that the interpreter will generate code in the loop to call __next__()
over and over again.  However, in the debugger you will see it step through the "powers()" function intead.  The
debugger will return execution to the calling program whenever it hit a "yield" instruction.  This corresponds to
the return statement in the hidden __next__() method.  

The body of the loop will then be executed and __next__() called again.  In the debugger this will be indicated 
by the debugger resuming execution of the "powers()" function on the line immediately after the "yield".

Things continue like this until x >= 1000, when the iterator will raise the StopIteration exception.  The debuuger
indicates this by hitting the return statement in "powers()".

So realise that the debugger can't show you what is really going on, but it does the best it can.

One further point, the iterator is created by the run-time when "powers()" is first called.  In the debugger, you
will find you can't step into the line:
            g = powers()
because this doesn't call the function (it creates the iterator object instead).
'''



def powers():
    x = 1
    while(x < 1000):
        x = x * 2
        yield x
        pass        # just to show execution resumes after the yield
    return

# calling the function produces a generator object, which is also an iterator
# note: calling the function does NOT execute the code in the function
g = powers()        # you can't step into powers() here
print(g)

# check that g has both iterator methods
print("Does g have an '__iter__' function:", hasattr(g, "__iter__"))
print("Does g have an '__next__' function:", hasattr(g, "__next__"))

# check the identity of the generator object
print(f"id of generator: {id(g):x}")
# check the identity of the object returned by __iter__() is the same
i = g.__iter__()
print(f"id returned by __iter__(): {id(i):x}")

# call __next__ directly (discouraged)
print(g.__next__(), end=", ")
print(g.__next__(), end=", ")

# use the global function next (recommended)
print(next(g), end=", ")
print(next(g))

# use g in a loop as an iterator
for n in g:      #  powers() instantiates a new generator
    print(n, end=", ")
print()

# use g in a loop as an iterator
for n in powers():      #  powers() instantiates a new generator
    print(n, end=", ")
print()
    
