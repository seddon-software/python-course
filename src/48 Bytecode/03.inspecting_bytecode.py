'''
Inspecting Bytecode
===================

We can look at the byte code for the function square using the comprehension shown below.  
The disassembler (dis) shows each bytecode in human readable form.  At the end of the program we print the 
bytecodes in hex using the comprehension:
            [hex(x) for x in square.__code__.co_code]
'''

from math import sqrt
import dis

def square(x,y):
    sq = sqrt(x**2 + y**2)
    return sq



# disassemble function square
dis.dis(square)

# now look at hex
print("\nprint the bytecode in hex:")
bytecode = [hex(x) for x in square.__code__.co_code]
print(", ".join(bytecode))

