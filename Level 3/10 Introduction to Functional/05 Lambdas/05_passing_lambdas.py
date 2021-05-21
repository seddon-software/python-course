# this lambda can take a lambda as a parameter
f = lambda x, func: func(x)

# invoke the lambda
print(f(10, lambda x:x**2))

# an equivalent call
print((lambda x:x**2)(10))



