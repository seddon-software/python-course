'''
CPython is both a Compiler and Interpreter
==========================================

CPython is both a compiler and interpreter.  The compiler translates source code into bytecode and the 
interpreter executes the code.  Each operating system has a different interpreter that understands native
code for that system.  Most of the work in running a Python program is done by the interpreter.  The compiler
stage is relatively simple.

Here we have a function that adds z and y.  Note that the bytecode produced by the compiler is the same for
two integers as it is for two strings.  All the work is done by the BINARY_ADD opcode.  However, what we can't
easily see is how BINARY_ADD works in the interpreter.  It turns out that BINARY handles the two cases very 
differently.  But to see that, we would need to look at the C code inside CPython.  Unfortunately the code is
too complicated to show here.

Older code from Python2 was a little easier to understand.  We reproduce it here to illustrate how the two cases
are handled very differently in the interpreter.  Don't worry about the details, just observe that PyInt is used
in CPython for integers and PyString for strings.  Line 20 checks for integers and then executes code in lines 21
to 31.  Line 33 checks for strings and then executes code via the function string_concatenate that is called in 
line 36: 

   case BINARY_ADD:
            w = POP();
            v = TOP();
            if (PyInt_CheckExact(v) && PyInt_CheckExact(w)) {
                /* INLINE: int + int */
                register long a, b, i;
                a = PyInt_AS_LONG(v);
                b = PyInt_AS_LONG(w);
                /* cast to avoid undefined behaviour
                   on overflow */
                i = (long)((unsigned long)a + b);
                if ((i^a) < 0 && (i^b) < 0)
                    goto slow_add;
                x = PyInt_FromLong(i);
            }
            else if (PyString_CheckExact(v) &&
                     PyString_CheckExact(w)) {
                x = string_concatenate(v, w, f, next_instr);
                /* string_concatenate consumed the ref to v */
                goto skip_decref_vx;
            }
            else {
              slow_add:
                x = PyNumber_Add(v, w);
            }
            Py_DECREF(v);
          skip_decref_vx:
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

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



