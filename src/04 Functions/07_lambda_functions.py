# lambda functions are an alternative to def's
# lambdas are expressions (not statements) and are often used as function parameters


# def's can have a body (but this function doesn't have a body)
def f(a, b, c):
    return a + b + c


# lambda's are not allowed to have a body
# this is equivalent to the function above
f = lambda a, b, c: a + b + c
