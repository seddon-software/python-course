# Closures close over variables, not values

############################################################
# Part 1 - closure fails
def outer():
    x = 50
    def inner():
        # outer 'x' is not in scope here
        # hence exception raised
        x += 1  # x refers to local x in inner because of +=, so NO closure
    return inner

f = outer()     # f now points to inner
try:
    f()         # calls inner()
except UnboundLocalError as e:
    print(e)


############################################################
# Part 2 - workaround for the above problem

def outer():
    x = [50]     # x is mutable
    def inner():
        # outer 'x' is brought into scope by the closure
        # hence NO exception raised
        x[0] += 1  # x refers to outer 'x' because its mutable => closure
        print(f"{str(x)}")
    return inner

f = outer()
try:
    f()
except UnboundLocalError as e:
    print(e)
