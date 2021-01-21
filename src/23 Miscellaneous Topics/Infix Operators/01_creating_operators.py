from functools import partial

class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)


@Infix
def add(x, y):
    return x + y

@Infix
def Δ(x, y):
    return x + y

@Infix
def ꞈ(x, y):
    return x + y


print(chr(0x394))
print(chr(0xff3e))
print(chr(0x221a))

z  = [1, 2] + [3, 4] 
print(z)

x = 5 |add| 6
print(x)

y = 5 |Δ| 6
print(y)

z = 5 |ꞈ| 6
print(z)

instanceof = Infix(isinstance)
if 5 |instanceof| int:
    print("yes")

curry = Infix(partial)

def f(x, y, z):
    return x + y + z

print(f |curry| 3)

g = f |curry| 3 |curry| 4 |curry| 5
print(g())
