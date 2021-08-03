import sys, os, re
sys.path.append("../src")  

def modifyPythonPathWithStage():
    base = "../src/build/"
    # search for directory begining with 'lib'
    for root, dirs, files in os.walk(base):
        for dir in dirs:
            if re.search(r"^lib", dir) != None: 
                stage = dir
    try:
        sys.path.append(base + stage)
    except:
        print("must build application first")
        sys.exit()
        
            
modifyPythonPathWithStage()            
import _myexample

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
