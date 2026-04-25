class BadInput(Exception): pass

class Calculator():
    def add(self, x, y):
        if not isinstance(x, (int, float)):
            raise BadInput() 
        if not isinstance(y, (int, float)):
            raise BadInput() 
        return x + y
        

