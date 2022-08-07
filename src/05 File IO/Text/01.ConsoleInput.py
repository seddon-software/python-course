'''
Console Input
=============
Use the input statement to read in data.  Note that input always reads in a string.  You have to use a cast
the input if you need a type such as int. 
'''

# arithmetic fails because x is a str
try:
    x = input("Enter an integer: ")
    print(f"type of x: {type(x)}")
    print(x + 20)
except Exception as e:
    print(e)

# arithmetic works if input is cast to an int
try:
    x = int(input("Enter an integer: "))
    print(f"type of x: {type(x)}")
    print(x + 20)
except Exception as e:
    print(e)


