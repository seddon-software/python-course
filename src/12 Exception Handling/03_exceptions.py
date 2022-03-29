'''
Exceptions
==========
The tag classes defined in the previous example won't allow you to pass an error message when the exception is 
raised.  If you want to allow your tag classes to accept messages, then you need to add an "__init__()" method
in your classes that delegate to the "__init__()" method in the "super" class as shown below.
'''

# define two tag classes that inherit from Exception
class TooBig(Exception): 
    def __init__(self, message): 
        super().__init__(message)       # delegate to Exception.__init__()
class MuchTooBig(Exception): 
    def __init__(self, message): 
        super().__init__(message)       # delegate to Exception.__init__()

def main():
    """ try different values of x and y to trigger exceptions"""
    try:
        x = 400
        y = 0
        
        if x > 150:
            raise MuchTooBig("x is much too big")
        if x > 50:
            raise TooBig("x  is too big")
        print(f"x is {x}")
        print(f"x/y is {x/y}")
    except TooBig as e:
        print(f"{e}")
    except MuchTooBig as e:
        print(f"{e.__str__()}")
    except Exception as e:
        print(e)

main()
