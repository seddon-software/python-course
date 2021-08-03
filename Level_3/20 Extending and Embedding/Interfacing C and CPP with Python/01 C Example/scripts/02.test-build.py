import sys, os, re

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
import fibonacci
print((fibonacci.fib(10)))
print((fibonacci.fib(11)))
print((fibonacci.fib(12)))


