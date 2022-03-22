'''
Test Invalid Code
=================
Here is an invalid program that uses type hints.  

We run this example first and then do a static analysis with Mypy.
'''

############################################################
# 1) run the program
############################################################
def concat(x:str, y:str, z:str) -> str:
    result = x + y + z

print(concat(5, 7, 9))

############################################################
# 2) perform static analysis with Mypy
############################################################
import os
print(f"mypy {os.path.basename(__file__)}")
os.system(f"mypy {os.path.basename(__file__)}")
