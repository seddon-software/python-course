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

Traditionally, Python bytecode might contain something like:
    x = a + b
and the interpreter executes a fairly general-purpose ADD operation. It doesn't initially know whether a and b are integers, floats, 
strings, etc.  With the adaptive interpreter, Python starts with a generic operation. After it has seen the operation execute repeatedly, 
it can specialise it:

    generic operation
           ↓
    observe actual types
           ↓
    executed many times
           ↓
    specialise operation
           ↓
    fast path for those types

So if x = a + b is called thousands of times with integers, Python can effectively turn the relevant bytecode into something specialised 
for integer addition.  Python doesn't rewrite your Python source code, it modifies/specialises the bytecode execution machinery internally.

The adaptive interpreter has also evolved considerably.
    Python 3.11 — introduced the specialising adaptive interpreter.
    Python 3.12 — improved specialisation and execution mechanisms.
    Python 3.13 — introduced further interpreter work, including the experimental JIT in CPython builds.

Note: The adaptive interpreter is specifically a CPython feature.
'''

# N.B. THIS WON'T WORK AT DIAMOND
# run the specialist tool from the command line
import os, sys
if sys.version_info >= (3, 11):
    os.system("python --version")
    os.system("specialist add.py")
else:
    print("The specialist tool requires python 3.11+")


