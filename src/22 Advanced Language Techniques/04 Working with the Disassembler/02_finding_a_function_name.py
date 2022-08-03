'''
Finding a function name
=======================

As the previous example shows it's difficult to determine the pointer name used to access a function object.
In this example we use the inspect and dis modules to extract this information.
'''


import inspect
import dis
import re
import sys
import io
trace = True

def debug(text):
    if trace: print(f"DEBUG: {text}")

def f():
    '''this function prints its name, even if called through a new reference'''        
    # look at the stack frame that called us
    caller = inspect.stack()[1][0]
    # disassemble the stack frame and pick out the call
    sys.stdout = io.StringIO()
    dis.disassemble(caller.f_code, caller.f_lasti)
    text = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    debug(f"stack frame = {text}")
    match = re.search(r'LOAD_NAME.*\((.*?)\)\s+-->', text)
    name = match.group(1)       # the name used to call the function
    debug(f"function name = {name}")
    print(f"I was called through: {name}")

f()

# change the object reference
g = f
del f       # reference f is now invalid

# now call the function through the new reference
g()
