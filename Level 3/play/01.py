# stateless function
def square(x):
    return x**2

def nextOne(x):
    x += 1
    nextOne.a += 1
    print(x, nextOne.a)

nextOne.a = 10
nextOne(5)
nextOne(5)
nextOne(5)
nextOne(5)
