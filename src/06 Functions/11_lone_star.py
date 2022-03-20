'''
Lone Star
=========

# The lone star delimit positional parameters.  All parameters 
# thereafter must be passed as keyword arguments (kwargs)
'''


def f(a, b, *, c="c_default", d="d_default"):  # c, d must be passed by name
    print(a, b, c, d)
    
try:
    f("one", "two", "three", "four")        # c, d must be passed by name
except Exception as e:
    print(e)

# pass 2 positional and 2 kwargs
f("one", "two", c="three", d="four")

# pass 1 positional and 3 kwargs
f("one", b="two", c="three", d="four")

# pass 0 positional and 4 kwargs
f(a="one", b="two", c="three", d="four")

# use default kwargs
f(a="one", b="two")

# check on the dfault for kwargs
print(f.__kwdefaults__)