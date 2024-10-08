'''
Variadic Named Parameters
=========================
Variadic named parameters work in a similar way to their positional counterparts.

In a variadic function, the ** wraps a variable number of key-value pairs into a dict.
When the passing a dict to a variadic function ** unpacks the dict before the call is made.

When calling a function the ** will unwrap a dict
            result = volume(**d)
is equivalent to writing:
            result = volume('height':12, 'depth':20, 'width':30})

When a function is called, the ** works the other way round
            result = volume('height':12, 'depth':20, 'width':30})
            def volume(**d):     # wraps up inputs into a dict

Positional parameters are often called args:
            *args       variable number of arguments
and key-value pairs are often called kwargs:
            *kwargs     variable number of keyword arguments
'''

def volume(*args, **kwargs):    # **kwargs wraps as a dict
    print(args, type(args))
    print(type(kwargs), kwargs)
    return (kwargs['height']+2)*(kwargs['width']+10)*kwargs['depth']

YmyDict = { 'height':12, 'depth':20, 'width':30, 'junk':88 }
print(volume(77, 88, 99, **myDict))   # ** unpacks the dict
print(volume(width=30, height=12, depth=20)) 


