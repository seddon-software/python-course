import sys, os, re
sys.path.append("../src")  


import myexample

myexample.say_hello("World")
myexample.say_goodbye("Universe")

iv = myexample.IntVector(4)
dv = myexample.DoubleVector(7)

for i in range(0,4):
    iv[i] = i * 100    
print(myexample.average(iv))

for i in range(0,7):
    dv[i] = float(i * 100)    
print(myexample.average2(dv))
