import os; os.system("clear")

x = input("Enter an integer: ")
print(x)
print(type(x))

# print(x + 100) # won't work because x is a string
print(int(x) + 100)