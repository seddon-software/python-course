def square(x):
    if not isinstance(x, int):
        raise Exception("x is not an int")
    return x**2

try:
    print( square(7) )
    print( square("seven") )
except Exception as e:
    print(e)

1