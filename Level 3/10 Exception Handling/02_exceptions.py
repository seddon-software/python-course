# define two tag classes
class TooBig(Exception): pass
class MuchTooBig(Exception): pass

def main():
    """ try different values of x and y to trigger exceptions"""
    try:
        x = 100
        y = 0
        
        if x > 150:
            raise MuchTooBig()
        if x > 50:
            raise TooBig()
        print(f"x is {x}")
        print(f"x/y is {x/y}")
    except TooBig as e:
        print(f"--{e}--")
        print("x is too big")
    except MuchTooBig as e:
        print("x is much too big")
    except Exception as e:
        print(e)


main()
