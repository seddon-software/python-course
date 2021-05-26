############################################################
#
#    try-except-else statements
#
############################################################

from math import sqrt
 

try:
    x = int(input("Enter positive integer: "))
    root = sqrt(x)
except Exception as e:
    print("sqrt() failed ...")
    print(e)
else:
    print("sqrt() succeeded ...")
    print(root)
 

