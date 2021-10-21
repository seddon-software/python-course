import os; os.system("clear")

# define two tag classes
class TooBig(Exception): 
    def __init__(self, message): 
        super().__init__(message)
class MuchTooBig(Exception): 
    def __init__(self, message): 
        super().__init__(message)

def main():
    """ try different values of x and y to trigger exceptions"""
    try:
        x = 81
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
