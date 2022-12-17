import inspect
from pprint import pprint


def f(x, y):
    pprint(inspect.stack())
    return x + y

def g(fn):
    def h(x, y):
        fn(x, y)
    return h

g(f)(5, 6)

        
