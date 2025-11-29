'''
There is a useful tool that you can use to visually see where the code is getting specialised without having 
to dig around in the bytecode. It's called specialist (requires Python 3.11+) and you can get it from pypi

    pip install specialist


The accompanying file: add.py contains:

x = 100
y = 200
for i in range(1000):
    x += 1
    y = y + x

print(x, y)

The specialist tool will run the script with python, then analyse the bytecode to calculate which lines 
were specialised. It will then open a web browser with the output (look for code highlighted in green).
'''

# N.B. THIS WON'T WORK AT DIAMOND
# run the specialist tool from the command line
import os, sys
if sys.version_info >= (3, 11):
    os.system("python --version")
    os.system("specialist add.py")
else:
    print("The specialist tool requires python 3.11+")


