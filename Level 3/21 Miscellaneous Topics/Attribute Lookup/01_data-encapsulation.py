# using a double underscore makes an attribute 'private'
# in practice the name is simply obfuscated as shown below
# and this doesn't really work

class Point:
    def __init__(self,x0,y0):
        self.__x = x0
        self.__y = y0        
    
# create object
point = Point( 50, 300)
print(point.__dict__)

# try to access private data
try:
    x = point.__x
    y = point.__y
except:
    print("statement failed")

try:
    print(point._Point__x)
    print(point._Point__y)
except:
    print("statement failed")


1
