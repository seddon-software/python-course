############################################################
#
#    if statements
#
############################################################

import math

x = 100

# simple statement
if x < 0:
    print('Negative')
else:   
    print('positive')

# compound statement
if x > 0:
    print('x is positive')
    print('the square of x is', x * x)
    print('the cube of x is', x * x * x)

# multi-branch (case statement)
if x < 0:
    print('Negative')
elif x == 0:
    print('Zero')
elif x == 1:
    print('One')
else:
    print('Greater than one')

# nested
if x > 0:
    print('x is positive')
    print('the square of x is', x * x)
    if x > 10:
        print('the square root of x is', math.sqrt(x))

# conditional expressions
result = (-1 if x < 0 else 1)
print(result)
