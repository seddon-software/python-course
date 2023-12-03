'''
The function parameter syntax(/) is to indicate that some function parameters must be specified 
positionally and cannot be used as keyword arguments (new in Python 3.8)
'''

def f(a, /, b, *, c, d):
    # a must be passed by position
    # b can be passed by position or keyword
    # c and d must bepassed by keyword

    print(a, b, c, d)

f(1, b=2, c=3, d=4)
f(1, 2, c=3, d=4)       
f(1, 2, c=3, d=4)
