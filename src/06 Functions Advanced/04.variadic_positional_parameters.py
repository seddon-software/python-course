'''
Variadic Positional Parameters
==============================
Sometimes you need to design a function that takes a variable number of parameters.  For instance, the 
"average()" function defined below can find the average of a variable number of parameters.  To allow for
such functions Python uses the * as follows.

When calling a function the * will unwrap a list or tuple such that
            result = average(*l)  # unwraps the list
is equivalent to writing:
            result = average(4, 6, 12, 5, 7, 3)

When a function is called, the * works the other way round
            result = average(4, 6, 12, 5, 7, 3)
            def average(*a):     # wraps up inputs into a tuple
'''

def average(*a):     # wraps up inputs into a tuple
    result = sum(a)/len(a)
    return result

result = average(4, 6, 12, 5, 7, 3)
print(result)

l = [4, 6, 12, 5, 7, 3]
result = average(*l)  # unwraps the list
print(result)
