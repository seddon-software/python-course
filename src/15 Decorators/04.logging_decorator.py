'''
Logging Decorator
=================

This time we allow the decorator to take a parameter:
            @log(logging.WARNING)
            def square(x): 

Python modifies the generated code to accomodate this parameter by providing an extra level of nested functions.
The parameter is passed to the outer function in the decorator and can be seen in both the inner functions by 
closure.  

The inner two functions follow the normal pattern with the decorator defining a new function (which it returns)
that calls the function being decorated.

Realise that this design was decided as the best way to allow decorators to accept parameters; remember that
the Python interpreter then modifies your code, such that, for example, a call to "square()":
            square(4)
            
when decorated as above, is translated to:
            log(logging.WARNING)(square)(4)
'''

import logging
import sys

# log(logging.WARNING)(square)(4)
#     returns logit(square)(4)
#         returns square(4)
#             returns 16

# define parameterized decorator
def log(level):
    def logit(fn):
        def enhance(x):
            message = f"calling {fn.__name__}({x})"
            if(level == logging.DEBUG):    logging.debug(message)
            if(level == logging.INFO):     logging.info(message)
            if(level == logging.WARNING):  logging.warning(message)
            if(level == logging.ERROR):    logging.error(message)
            if(level == logging.CRITICAL): logging.critical(message)
            return fn(x)
        return enhance
    return logit

@log(logging.DEBUG)
def square(x): 
    return x * x

@log(logging.WARNING)
def cube(x):
    return x * x * x

@log(logging.CRITICAL)
def quad(x):
    return x * x * x * x
    
# main program
# as no logfile specified, use the console
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(level=logging.CRITICAL)

# print( log(logging.WARNING)(square)(4) )
print(square(4))
print(cube(5))
print(quad(10))


