'''
Lambda Functions
================

Lambda functions are an alternative to using def's to define a function.  Lambdas are expressions (not statements)
and as such can be used wherever an expression is allowed.  Lambda functions are often used as parameters to other
functions.

A big difference between def's and lambda's is that the lambda is not permitted to have a function body.  This
restriction was introduced to keep lambdas simple (unlike languages like C++ where lambdas can have complex 
bodies).

Lambdas define an anonymous function.  In the line
            f = lambda a, b, c, d: a + b + c + d
the anonymous function object is assign to the pointer f.  Once this is done, the function can be called in the 
normal way:
        f(1, 10, 100, 1000)

Note the syntax of a lambda is
        lambda <input-parameters> : <return-value>
        
which is equivalent to a def with no body:
        def <name>(<input-parameters>):
            return <return-value>
'''



# def's can have a body
def f(a, b, c, d):
    print("this is the body of function f")
    return a + b + c + d


# lambda's are not allowed to have a body
# this is equivalent to the function above (minus the body)
fn = lambda a, b, c, d: a + b + c + d

# call the lambda
result = fn(1, 10, 100, 1000)
print(result)
