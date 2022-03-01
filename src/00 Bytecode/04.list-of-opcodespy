'''
AS we know, CPython is written in C.  Opcodes are stored in a C header file called opcode.h.  Run this script to 
see the first few opcodes (the first few lines in the file are C code and irrelevant, so by using tail we will 
omit these lines).  This header file is for Python 3.10.2.
'''

import os
numberOfOpcodes = 20
skipLines = 9
os.system(f"head -{numberOfOpcodes + skipLines} opcode.h | tail -{numberOfOpcodes}")
