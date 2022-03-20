'''
Variadic Positional Parameters
==============================
'''

def average(*a):     # wraps up inputs into a tuple
    print(a, type(a))
    a = list(a)
    print(a, type(a))
    result = sum(a)/len(a)
    return result

l = [4, 6, 12, 5, 7, 3]
result = average(*l)  # unwraps the list
print(result)
result = average(4, 6, 12, 5, 7, 3)
print(result)
