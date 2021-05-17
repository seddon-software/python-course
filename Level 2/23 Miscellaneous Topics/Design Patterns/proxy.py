class Subject:
    def square(self, x):
        return x * x
    
    def average(self, x, y):
        return (x + y)/2.0
        
class Proxy:
    # static data
    subjectMethod = None
    
    # link proxy to subject
    def __init__(self, subject):
        self.subject = subject
    
    # called if method not found on proxy
    def __getattr__(self, method):
        # save subjectMethod 
        Proxy.subjectMethod = getattr(self.subject, method)
        # return static method to call
        return Proxy.__delegate
    
    @staticmethod
    def __delegate(*args):
        # trace call
        name = Proxy.subjectMethod.__name__
        params = ','.join(str(arg) for arg in args)
        print("calling: " + name + "(" + params + ")")
        
        # retreive subject method and call it
        result = Proxy.subjectMethod(*args)        
        return result
        
        
        
obj = Proxy(Subject())
x = obj.average(10, 12.5)
print("result =", x)
print()

x = obj.square(5)
print("result =", x)




1