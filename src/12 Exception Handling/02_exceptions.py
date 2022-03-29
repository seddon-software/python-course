'''
Exceptions
==========
Rather than use the Exception class to raise exceptions, you might prefer to raise user defined exceptions.  In
this example we define two "tag" classes: 
        class TooBig(Exception): pass
        class MuchTooBig(Exception): pass

A tag class is one that doesn't add any functionality to the Exception class, but does have a different name.
This allows you to catch your objects of your tag classes rather than those of the Exception class:
            except TooBig as e:
                print("x is too big")
            except MuchTooBig as e:
                print("x is much too big")
'''

# define two tag classes
class TooBig(Exception): pass
class MuchTooBig(Exception): pass

def main():
    """ try different values of x and y to trigger exceptions"""
    try:
        x = 400
        y = 0
        
        if x > 150:
            raise MuchTooBig()
        if x > 50:
            raise TooBig()
        print(f"x is {x}")
        print(f"x/y is {x/y}")
    except TooBig as e:
        print("x is too big")
    except MuchTooBig as e:
        print("x is much too big")
    except Exception as e:
        print(e)

main()
