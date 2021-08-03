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
        
sys.path.append('../..')
import set_paths
            
modifyPythonPathWithStage()            

import boost_example

print(boost_example.printArray())
print(boost_example.greet())
print(boost_example.average(5.0, 6.0))


