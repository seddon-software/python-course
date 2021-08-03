# conventional function that takes 5 args
def func(a, b, c, d, e):
    return a, b, c, d, e

print(func(1, 2, 3, 4, 5))

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
print(a(2)(3)(4)(5))
print(b(3)(4)(5))
print(c(4)(5))
print(d(5))
print(e)



 