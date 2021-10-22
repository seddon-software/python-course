x = 10
a = 50
b = 100

if x > a:              # note colon
    print("x is > ", a) # note indentation (4 spaces)

if x > a:              # indentation must be the same for all statments in body
    print("x is > ", a)
    print("x is > ", a)
    print("x is > ", a)

if x > a:              # can have an else branch
    print("x is > ", a)
    print("x is > ", a)
    print("x is > ", a)
else:
    print("x is <= ", a)
    print("x is <= ", a)
    print("x is <= ", a)

if x > b:              # can have an elif branch (note order of comparisons)
    print("x is > ", b)
elif x > a:
    print("x is > ", a)
else:
    print("x is <= ", a)

