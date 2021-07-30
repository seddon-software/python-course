# lambda functions are an alternative to def's
# lambdas are expressions (not statements) and are often 
# used as function parameters


# def's can have a body
def f(a, b, c, d):
    print("this is the body of function f")
    return a + b + c + d


# lambda's are not allowed to have a body
# this is equivalent to the function above (minus the body)
f = lambda a, b, c, d: a + b + c + d

# call the lambda
result = f(1, 10, 100, 1000)
print(result)
