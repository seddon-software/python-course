'''
Currying
========

Currying is the transformation of a function with multiple arguments into a sequence of single-argument functions.
That means converting a function like this f(a, b, c, ...) into a function like this f(a)(b)(c)... 
'''

# conventional function that takes 5 args
def func(a, b, c, d, e):
    return a, b, c, d, e

print(func(10, 20, 30, 40, 50))

# curried version that takes 1 arg
def f(a):
    def g(b):
        def h(c):
            def i(d):
                def j(e):
                    return a, b, c, d, e
                return j
            return i
        return h
    return g
 
# f can be called in a variety of ways
a = f(1)
b = f(1)(2)
c = f(1)(2)(3)
d = f(1)(2)(3)(4)
e = f(1)(2)(3)(4)(5)

# missing arguments can be supplied later
print(a(20)(30)(40)(50))
print(b(30)(40)(50))
print(c(40)(50))
print(d(50))
print(e)



 