import json

# classes to encode and decode
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        print("Point:", self.x, ":", self.y)

class My3Tuple:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
    def display(self):
        print("My3Tuple:", self.x1, self.x2, self.x3)

# JSON encoder
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        # Convert objects to a dictionary of their representation
        d = {}
        d['__class__'] = obj.__class__.__name__
        d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return d

# JSON decoder
class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            print('MODULE:', module)
            class_ = getattr(module, class_name)
            print('CLASS:', class_)
            args = dict( (key, value) for key, value in list(d.items()))
            print('INSTANCE ARGS:', args)
            print()
            
            # this assumes constructor takes parameters with the same names as fields
            inst = class_(**args)
        else:
            inst = d
        return inst
    
# create encoder and decoder
encoder = MyEncoder()
decoder = MyDecoder()

# sample objects
l1 = [3, 5, 7, 9]
p1 = Point(5, 8)
t1 = My3Tuple(2,4,6)

#encode objects as JSON strings
lJSON = encoder.encode(l1)
pJSON = encoder.encode(p1)
tJSON = encoder.encode(t1)
print(lJSON)
print(pJSON)
print(tJSON)

# decode JSON strings
l2 = decoder.decode(lJSON)
p2 = decoder.decode(pJSON)
t2 = decoder.decode(tJSON)
print(l2)
p2.display()
t2.display()

1