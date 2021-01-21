# define a finite generator
def fibonacci(max):
    a, b = 0, 1
    while(b < max):
        yield b
        a, b = b, a+b

# use generator in a loop
for x in fibonacci(100):
    print(x, end=' ')
print()

# generator can be evaluated to a tuple
t = tuple(fibonacci(100))
print(t)

# generator can be evaluated to a list
l = list(fibonacci(100))
print(l)
