'''
Now we return to our original problem: how to access an attribute after the function object reference is changed.
We used the example we saw earlier which retreives the function name independent of the reference used.
'''


import inspect
import dis
import re
import sys
import io

trace = False


def debug(text):
    if trace: print(f"DEBUG: {text}")

def f():
    '''this function returns its x attribute even if the function's name changes
       by using the inspect and dis modules'''        
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

    # now extract the x attribute value
    try:
        # now we know the reference name we can access the locals
        func = caller.f_locals[name]
        debug(f"locals = {func}")
        debug(f"x = {func.x}")
    except KeyError:
        func = caller.f_globals[name]
    print(f"{name}.x attribute = {func.x}")

# set up a function with an attribute x
f.x = 'foo'
f()

# change the object reference
g = f
del f       # reference f is now invalid

# now call the function through the new reference
g()

