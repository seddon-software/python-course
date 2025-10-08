'''
Passing lambda as Parameters
============================

lambdas are anonymous functions and as such can be passed as a parameter to another function.  This
is what is happening in this example.  

Here, "func" is passed as a lambda inside "f".  When "f" is called as in:
            f(10, lambda x:x**2)

"func" is pointing at lambda x:x**2.

The return value of the "f" is "func()".  The brackets mean the lambda will be called immediately as part of 
this return.
'''

# this lambda takes a function pointer and an input parameter for the function pointer ...
# ... and then invokes the function
f = lambda x, func: func(x)     # calls func in the return

# invoke the lambda
print(f(10, lambda x:x**2))     # will call lambda x:x**2 with x = 10 

# an equivalent call
print((lambda x:x**2)(10))



