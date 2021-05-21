import dis

# the compiler generates bytecode for this function
# and the interpreter works out what to do with each opcode
def f(x, y):
    return x + y

print( f("ABC", "DEF") )
print( f(5, 7) )

# look at the bytecode
dis.dis(f)

# the disassembler generates the following
'''
  6           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD          
              6 RETURN_VALUE 
'''
# note how BINARY_ADD is interpreted differently for the case of str and int



