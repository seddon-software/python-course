import os; os.system("clear")
'''
CPython is both a Compiler and Interpreter
==========================================

CPython is both a compiler and interpreter.  The compiler translates source code into bytecode and the 
interpreter executes the code.  Each operating system has a different interpreter that understands native
code for that system.  Most of the work in running a Python program is done by the interpreter.  The compiler
stage is relatively simple.

Here we have a function that adds x and y.  Note that the bytecode produced by the compiler works for both
integers and strings.  All the work is done by the BINARY_ADD opcode.  However, what we can't easily see is 
how BINARY_ADD works in the interpreter.  It turns out that BINARY handles the two cases very differently.  
But to see that, we would need to look at the C code inside CPython.  

The CPython interpreter is open source and you can read through it on GitHub. The implementation of the bytecode 
interpreter is in the file Python/ceval.c.  In the Python 3.6.4 release the bytecode instructions are handled by 
a switch statement beginning on line 1266.  The bytecode for BINARY_ADD begins on line 1475 and is reproduced 
below (https://github.com/python/cpython/blob/d48ecebad5ac78a1783e09b0d32c211d9754edf4/Python/ceval.c)

We reproduce it here to illustrate how the two cases are handled in the interpreter.  Don't worry about the 
details, just observe that PyNumber is used for numbers and PyUnicode for strings.  Note how the unicode and 
number parts are handled very differently.

        TARGET(BINARY_ADD) {
            PyObject *right = POP();
            PyObject *left = TOP();
            PyObject *sum;
            if (PyUnicode_CheckExact(left) &&
                     PyUnicode_CheckExact(right)) {
                sum = unicode_concatenate(left, right, f, next_instr);
                /* unicode_concatenate consumed the ref to left */
            }
            else {
                sum = PyNumber_Add(left, right);
                Py_DECREF(left);
            }
            Py_DECREF(right);
            SET_TOP(sum);
            if (sum == NULL)
                goto error;
            DISPATCH();
        }

If you are interested in bytecode, check out:
            https://opensource.com/article/18/4/introduction-python-bytecode
'''

import dis

# the compiler generates bytecode for this function
# and the interpreter works out what to do with each opcode
def add(x, y):
    return x + y

print( add("ABC", "DEF") )
print( add(5, 7) )

# look at the disassembled bytecode
dis.dis(add)

# the disassembler generates the following
'''
  6           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD          
              6 RETURN_VALUE 
'''
# note: BINARY_ADD is interpreted differently for str and int



