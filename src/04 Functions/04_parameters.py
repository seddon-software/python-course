############################################################
#
#    default parameters
#
############################################################


# parameters can be positional or named (or a combination of both)

def f(a, b, c):
    return a + b + c

# positional parameters
print(f(1, 1, 1), end=' ')
print(f(1, 2, 3), end=' ')
print(f(2, 4, 8))

# named parameters
print(f(a = 1, b = 1, c = 1), end=' ')
print(f(c = 3, a = 1, b = 2), end=' ')
print(f(c = 8, b = 4, a = 2))
