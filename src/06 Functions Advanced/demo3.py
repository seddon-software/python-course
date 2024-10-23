def volume(*args, **kwargs):        # pack
    return  kwargs['h'] * (kwargs['w'] + 5) * (kwargs['d'] + 10)

print( volume(h=3, w=5, d=7) )
print( volume(d=7, w=5, h=3) )
myDict = {'h':3, 'w':5, 'd':7, 'junk':99}
print(volume(1, 2, 3 , **myDict))       # unpack