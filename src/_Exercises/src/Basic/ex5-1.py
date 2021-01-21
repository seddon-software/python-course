"""
Write a program that calculates the factorial of an integer 
in the range 2 to 10.  Add exception handling code to prevent 
calculating a result where the input number is larger than 10, 
or any negative integer.  Make sure you can handle the case 
where the input is not an integer.
"""

try:
    x = int(input("Enter an integer for factorial calculation: "))
    if x > 10: raise Exception(f"number too large: {x}")
    if x <  2: raise Exception(f"number too small: {x}")
except Exception as e:
    print(e)
    exit(1)

result = 1
for i in range(1, x+1):
    result = result * i
    
print(f"Factorial of {x} = {result}")


