############################################################
#
#    closures
#
############################################################

# define a closure containing width and precision
def printWithPrecision(width, precision):
    def printIt(x):
        print(f"{x:{width}.{precision}f}")
    return printIt

print10dot3 = printWithPrecision(10, 3)
print8dot2 = printWithPrecision(8, 2)
print6dot1 = printWithPrecision(6, 1)

x = 1234.56789
y = 9876.54321

print10dot3(x)
print10dot3(y)
print8dot2(x)
print8dot2(y)
print6dot1(x)
print6dot1(y)
1
