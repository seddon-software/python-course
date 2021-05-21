# Closures close over variables, not values

############################################################
# Part 1 - closure fails
def outer():
    x = 50
    def inner():
        print((inner.__closure__))
        x += 1  # x refers to local x => NO closure
    return inner

f = outer()
try:
    f()     # outer 'x' is not in scope here
            # hence exception raised
except UnboundLocalError as e:
    print(e)

print()

############################################################
# Part 2 - workaround for the above problem

def outer():
    x = [50]     # x is mutable
    def inner():
        print((inner.__closure__))
        print((inner.__closure__[1].cell_contents))
        x[0] += 1  # x refers to outer 'x' because its mutable => closure
    return inner

f = outer()
try:
    f()     # outer 'x' is brought into scope by the closure
            # hence NO exception raised
except UnboundLocalError as e:
    print(e)
