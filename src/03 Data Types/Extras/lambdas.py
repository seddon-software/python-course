def f(x):                # f is the pointer, the bytecode in the function is the object
    return x * x
print(id(f))

f = lambda x : x * x
print(id(f))

print(f(6))
print(f(7))


