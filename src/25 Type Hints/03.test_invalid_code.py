'''
Test Invalid Code
=================
Here is an example of an invalid program that uses type hints.  Note that the type hints are ignored at runtime
and the program executes without throwing an exception.  However, the static analysis uncovers the error with
the wrong types of parameters pased to the routine (int instead of str).  

We run this example first and then do a static analysis with mypy.
'''

############################################################
# 1) run the program
############################################################
def concat(x:str, y:str, z:str) -> str:
    result = x + y + z
    print(result)

concat(5, 7, 9)

############################################################
# 2) perform static analysis with mypy
############################################################
import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
