############################################################
#
#    closures
#
############################################################

# define a closure containing width and precision
def printWithPrecision(width, precision):
    def printIt(x):
        print("{2:{0}.{1}f}".format(width, precision, x))
    return printIt

print10dot3 = printWithPrecision(15, 6)
print8dot2 = printWithPrecision(8, 1)
print7dot1 = printWithPrecision(7, 9)

x = 1234.56789
y = 9876.54321

print10dot3(x)
print10dot3(y)
print8dot2(x)
print8dot2(y)
print7dot1(x)
print7dot1(y)
1
