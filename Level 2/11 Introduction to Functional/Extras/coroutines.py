def mycoroutine(func):
    def start():
        cr = func() # create the iterator
        next(cr)   # get to first yield
        return cr   # return the iterator
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
        parameters = yield
        message = parameters.pop(0)
        for decorator in parameters:
            g = decorator() # return the iterator
            message = g.send(message)
        print(message)
    
g = format()        # return an iterator
g.send(["MiXeD", upper, bold, italic])
g.send(["MiXeD", lower])
g.send(["MiXeD", italic, upper])
