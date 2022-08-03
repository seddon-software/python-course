'''
With Clause
===========
The usage of resources such as files, locks, database connections needs to be carefully managed.  You must make
sure to release these resources after usage. If they are not released then it will lead to resource leakage and 
may cause the system to either slow down or crash. 

In Python, you can use a "with" statement to ensure resources are automatically released after use.  The language
provides a number of resource allocation cases that support "with", but you can define your own; these are called 
context managers.

To define a context manager you must add the following methods to your class:
            def __enter__(self):
            def __exit__(self, type, value, traceback):

Here we show how to do this and also show the equivalent code that is produced when using "with".  If an
exception if thrown you will get full access to the traceback info (see "traceback" in Python docs). 
'''

import sys

class MyException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
        
class MyClass:
    def __enter__(self):
        print("WITH: initialization")
        return self # object to be used in with clause
    
    def __exit__(self, type, value, traceback):
        print("WITH: cleanup")
        print("type:     ", type)
        print("value:    ", value)
        print("traceback:", traceback)
        return False  # propagate exception (True swallows the exception)

    def hello(self):
        print("Hello")

    def oops(self):
        raise MyException("oops")

print("============ WITH ==========================")        
try:
    with MyClass() as m:
        m.hello()
        m.oops()
except Exception as e:
    print("exception propagated out of with statement")

print("\n\n============ Equivalent Code ===============")        
try:
    try:
        m = MyClass().__enter__()
        m.hello()
        m.oops()
    except Exception as e:
        traceback = sys.exc_info()
        result = m.__exit__(type(e), e, traceback[-1])
        if not result: raise 
    else:
        m.__exit__(None, None, None)
except Exception as e:
    print("exception propagated out of with statement")

