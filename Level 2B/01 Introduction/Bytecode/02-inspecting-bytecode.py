from math import sqrt

# function to analyse
def square(x,y):
    sq = sqrt(x**2 + y**2)
    return sq

import opcode
def translate(instruction):
    print(f"{instruction} = {hex(opcode.opmap[instruction])}")

# print opcodes
print(square.__code__)
print([ hex(x) for x in square.__code__.co_code] )

# list opcodes
translate('LOAD_GLOBAL')
translate('LOAD_FAST')
translate('LOAD_CONST')
translate('BINARY_POWER')
translate('BINARY_ADD')
translate('CALL_FUNCTION')
translate('STORE_FAST')
translate('RETURN_VALUE')

# print disassembly
import dis
dis.dis(square)



