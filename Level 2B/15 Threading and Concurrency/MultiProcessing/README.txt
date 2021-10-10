According to the Python documention you must make sure that the main module 
can be safely imported by a new Python interpreter without causing unintended 
side effects (such a starting a new process).

In practice this means using:

    if __name__ == '__main__': 
        code ...
        
as the start of main.
