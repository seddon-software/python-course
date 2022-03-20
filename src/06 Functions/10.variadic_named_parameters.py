'''
Variadic Named Parameters
=========================
Variadic named parameters work in a similar way to their positional counterparts.

On calling a variadic function, the ** unwraps a dict parameter into individual key-value pairs of parameters.
When the function is called that defines a **parameter, individual key-value pairs of parameters get wrapped into
a dict.

Positional parameters are often called args:
            *args       variable number of arguments
and key-value pairs are often called kwargs:
            *kwargs     variable number of keyword arguments
'''

def volume(*args, **kwargs):    # **kwargs wraps as a dict
    print(args, type(args))
    print(type(kwargs), kwargs)
    return (kwargs['height']+2)*(kwargs['width']+10)*kwargs['depth']

myDict = { 'height':12, 'depth':20, 'width':30, 'junk':88 }
print(volume(99, **myDict))   # ** unpacks the dict
print(volume(width=30, height=12, depth=20)) 


