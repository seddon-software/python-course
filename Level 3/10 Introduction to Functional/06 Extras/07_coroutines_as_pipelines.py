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
