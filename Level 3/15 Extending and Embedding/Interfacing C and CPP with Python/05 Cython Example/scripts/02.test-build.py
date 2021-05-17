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
import functions
functions.say_hello()
functions.say_goodbye()
print((functions.fibonacci(100000)))
print((functions.sumOfSquares(2, 4)))
