'''
Passing lambda as Parameters
============================

lambdas are anonymous functions and as such can be passed as a parameter to another function.  This
is what is happening in this example.  Note "func" is passed as a lambda.  The return value of the function
object pointed at by f invokes the lambda because of the ():
            func() 
'''
# this lambda can take a lambda as a parameter for func
f = lambda x, func: func(x)     # calls func as part of the return

# invoke the lambda
print(f(10, lambda x:x**2))     # will call lambda x:x**2 with x = 10 

# an equivalent call
print((lambda x:x**2)(10))



