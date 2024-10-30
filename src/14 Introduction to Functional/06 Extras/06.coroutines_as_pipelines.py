import os; os.system("clear")
'''
You can combine generators in a kind of pipeline where each generator operates on input data and
then passes the data to the next generator in line.  Recal that you must call a generator function
to create the generator and step through to the first "yield" before it is operational.  In this example 
we use a decorator to perform these tasks'''

# decorator that takes a generator as a parameter
def mycoroutine(generator):
    def start():
        iterator = generator() # invoke generator to create an iterator
        next(iterator)         # iterate to first yield
        return iterator        # return the iterator
    return start

    
@mycoroutine
def lower():    # a generator
    while True:
        message = yield
        yield message.lower()
    
@mycoroutine
def italic():   # a generator
    while True:
        message = yield
        yield "<i>" + message + "</i>"

@mycoroutine
def upper():    # a generator
    while True:
        message = yield
        yield message.upper()

@mycoroutine
def bold():     # a generator
    while True:
        message = yield
        yield "<b>" + message + "</b>"


@mycoroutine
def format():   # a generator
    while True:
        # get starting string and a set of iterating functions
        parameters = yield
        # print(parameters)

        # pop of the starting string (only coroutines remain)
        message = parameters.pop(0)

        # iterate through co-routines
        for decorator in parameters:
            cr = decorator() # return the coroutine
            message = cr.send(message)
        print(message)
    
g = format()        # return a format iterator
g.send(["MiXeD", upper, bold, italic])
g.send(["MiXeD", lower])
g.send(["MiXeD", italic, upper])
