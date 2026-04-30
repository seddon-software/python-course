import os; os.system("clear")
'''
Replacing Magic Numbers
=======================

Here is another example of defining nesting functions that define 3 formatting functions.
'''

# define a closure containing width and precision
def printWithPrecision(width, precision):
    def printIt(x):
        print(f"{x:{width}.{precision}f}")
    return printIt

print10dot3 = printWithPrecision(10, 3)
print8dot2 = printWithPrecision(8, 2)
print7dot1 = printWithPrecision(7, 1)

x = 1234.56789
y = 9876.54321

print10dot3(x)
print10dot3(y)
print8dot2(x)
print8dot2(y)
print7dot1(x)
print7dot1(y)

