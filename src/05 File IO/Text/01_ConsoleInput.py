try:
    x = input("Enter an integer: ")     # note: doesn't work in VSCode debug console
except Exception as e:
    print(e)

print(x)
print(type(x))

# print(x + 100) # won't work because x is a string
print(int(x) + 100)