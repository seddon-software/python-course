n = input("Please enter an integer: ")
print(type(n))
try:
    n2 = int(n)
    print(type(n2))
    print(n2 + 7)
except Exception as e:
    print("Enter an integer next time")
    print(e)
