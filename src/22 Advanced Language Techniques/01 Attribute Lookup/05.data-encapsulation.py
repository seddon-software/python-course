'''
Data Encapsulation
==================

Languages like C++ and Java enforce data encapsulation with the public and private keywords.  This ensures all
access to an object's attributes has to be via the methods defined in the class.  You can find a lot of discussions
on the web as to why this is a good idea - basically to make code more reliable and less fragile.

Python on the other hand has never provided similar facilities and probably never will.  Nevertheless, an
attempt was made to provide something similar way baci in Python 2 days and its still available.  The idea was
to restrict access to attributes that were defined with two leading underscores as in:
            self.__x
            self.__y       
While this appears to make the attributes private, it is easy to work around.  If you look at the object's 
dictionary you'll see immediately that Python has obfuscated the attribute names as follows:
            self._Point__x
            self._Point__y
by just prepending "_Point" to the names.  Once you know this has happened all you have do to access the 
attributes directly is to use the new name and the attributes are no longer private!       
'''

# using a double underscore makes an attribute 'private'
# in practice the name is simply obfuscated as shown below
class Point:
    def __init__(self,x0,y0):
        self.__x = x0
        self.__y = y0        
    
# create object
p = Point( 50, 300)
print(p.__dict__)

# try to access private data
try:
    print("accessing __x and __y")
    x = p.__x
    y = p.__y
except:
    print("statement failed")

try:
    print("accessing _Point__x and _Point__y")
    print(p._Point__x)
    print(p._Point__y)
except:
    print("statement failed")



