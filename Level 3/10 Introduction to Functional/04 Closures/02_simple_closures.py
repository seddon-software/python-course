############################################################
#
#    closures
#
############################################################


def f(x):
    def g(y, z):    # this function knows about the value of x
        return x + y + z
    return g

# or equivalently
def f(x):
    return lambda y,z:x+y+z # this knows about x

# or equivalently
f = lambda x: lambda y,z:x+y+z

f15 = f(15)   # f15 points to a function returning 15 + y + z
f20 = f(20)   # f20 points to a function returning 20 + y + z
f25 = f(25)   # f25 points to a function returning 25 + y + z
f50 = f(50)   # f50 points to a function returning 50 + y + z


print((f20(1,2)))  # prints 20 + 1 + 2
print((f20(7,9)))  # prints 20 + 7 + 9
print((f50(1,2)))  # prints 50 + 1 + 2
print((f50(7,9)))  # prints 50 + 7 + 9

