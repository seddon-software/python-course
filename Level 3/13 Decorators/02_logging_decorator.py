############################################################
#
#    decorators
#
############################################################

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

@log(logging.WARNING)
def square(x): 
    return x * x

@log(logging.DEBUG)
def cube(x):
    return x * x * x

@log(logging.CRITICAL)
def quad(x):
    return x * x * x * x
    
# main program
# as no logfile specified, use the console
logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(level=logging.CRITICAL)

# print( log(logging.WARNING)(square)(4) )
print(square(4))
print(cube(5))
print(quad(10))


