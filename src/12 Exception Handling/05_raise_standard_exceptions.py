'''
Raise Standard Exceptions
=========================
Python defines many standard exceptions which you are free to use in your code.  Check out the list at:
            https://docs.python.org/3/library/exceptions.html

Although you can use these exception classes, it often better to defined your own domain specific tag classes as
discussed earlier.
'''

array = [0,1,2,3,-4,5,6]

try:
    for x in array:
        if x < 0: 
            raise ValueError("array index is negative!")
        print(array[x], end=' ')
except ValueError as e:
    print(f"\n... entering except block: {e}")


