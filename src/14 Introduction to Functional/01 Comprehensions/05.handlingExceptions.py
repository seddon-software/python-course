import os; os.system("clear")
'''
Catching Exceptions
===================

If the comprehension raises an exception it will may cause the comprehension to fail.  What you can do is to
call a function that catches the exception locally so that the comprehension doesn't see the exception.

To illustrate, we create a sequence containing a zero and calculate reciprocals.  Obviously when we divide by zero
we will raise an exception.  The function "catch" (it can be called anything) handles this exception locally.  
Note how the function has access to its closure which includes "n"; therefore the "n" parameter does need to 
be passed to "catch" explicitly.  
'''

def catch(fn):  # fn captures n in the call
    try:
        return f"{fn():.2f}"  # fn = the lambda which takes no parameters
    except Exception as e:
        return e

# create a list containing zero
numbers = [float(n) for n in range(-5, 5)]
print(numbers)

# comprehension will raise an exception for a zero entry
reciprocals = [catch(lambda : 1/n) for n in numbers] # lambda captures n
print(f"{reciprocals}")
