############################################################
#
#    with clause
#
############################################################

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

print("============ Equivalent Code ===============")        
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

