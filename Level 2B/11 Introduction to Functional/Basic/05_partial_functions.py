import functools as ft

# return a new function which behaves like the original function with some parameters filled in

# range takes 3 parametrs
myrange = ft.partial(range, 0, 10) # 2 parameters filled in
print((list(myrange())))
print((list(myrange(2)))) # supply a 3rd parameter

# now try with a function of 5 parameters
def f(v, w, x, y, z): return v + w + x + y + z

f1 = ft.partial(f, 10, 20)
print((f1(30, 40, 50)))

f2 = ft.partial(f1, 30)
print((f2(40, 50)))
