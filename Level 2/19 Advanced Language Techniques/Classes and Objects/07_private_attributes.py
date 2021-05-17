# encapsulate attributes

class MyClass:
    def __init__(self):
        # data is fully encapsulated - can't be seen outside the class
        data = {}
        # these methods can access data by closure
        def dogetX(): return data['x']
        def dogetY(): return data['y']
        def dosetX(x): data['x'] = x
        def dosetY(y): data['y'] = y
        # these attributes belong to each object, not the class
        self.dogetX = dogetX
        self.dogetY = dogetY
        self.dosetX = dosetX
        self.dosetY = dosetY

m1 = MyClass()
m2 = MyClass()
m1.dosetX(100)
m1.dosetY(101)
m2.dosetX(200)
m2.dosetY(201)
print(m1.dogetX())
print(m1.dogetY())
print(m2.dogetX())
print(m2.dogetY())
