############################################################
#
#    function names
#
############################################################


import inspect
import dis
import re
import sys
import io

# how to access the name of the function reference, independent of 
# original function name

def f():
    '''this function prints its name, even if called through a new reference'''
        
    # look at the stack frame that called us
    caller = inspect.stack()[1][0]
    print(f"DEBUG: stack = {caller}")
    # disassemble the stack frame and pick out the call
    sys.stdout = io.StringIO()
    dis.disassemble(caller.f_code, caller.f_lasti)
    text = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    print(f"DEBUG: stack frame = {text}")
    match = re.search(r'LOAD_NAME.*\((.*?)\)\s+-->', text)
    name = match.group(1)       # the name used to call the function
    print(f"DEBUG: function name = {name}")
    print(f"I was called through: {name}")

# set up a function with an attribute x
f()

# change the object reference
g = f
del f       # reference f is now invalid

# now call the function through the new reference
g()
