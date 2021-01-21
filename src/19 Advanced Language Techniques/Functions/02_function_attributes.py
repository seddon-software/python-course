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

'how to access an attribute of a function, independent of original function name'

def f():
    '''this function returns its x attribute even if the function's name changes
       uses the inspect and dis modules'''
        
    # look at the stack frame that called us
    caller = inspect.stack()[1][0]
    
    # disassemble the stack frame and pick out the call
    sys.stdout = io.StringIO()
    dis.disassemble(caller.f_code, caller.f_lasti)
    text = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    match = re.search(r'LOAD_NAME.*\((.*?)\)\s+-->', text)
    name = match.group(1)       # the name used to call the function

    # now extract the x attribute value
    try:
        func = caller.f_locals[name]
    except KeyError:
        func = caller.f_globals[name]
    return func.x

# set up a function with an attribute x
f.x = 'foo'
print(('call f():', f()))

# change the object reference
g = f
del f       # reference f is now invalid

# now call the function through the new reference
print(('call g():', g()))
print((g.x))
