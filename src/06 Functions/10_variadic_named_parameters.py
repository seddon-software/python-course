'''
Variadic Named Parameters
=========================
'''

def volume(*args, **kwargs):    # wraps as a dict
    print(args, type(args))
    print(type(kwargs), kwargs)
    return (kwargs['height']+2)*(kwargs['width']+10)*kwargs['depth']

myDict = { 'height':12, 'depth':20, 'width':30, 'junk':88 }
print(volume(99, **myDict))   # ** unpacks the dict
print(volume(width=30, height=12, depth=20)) 


