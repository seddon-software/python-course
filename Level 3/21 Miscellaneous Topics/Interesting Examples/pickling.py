############################################################
#
#    pickling
#
############################################################

import pickle

s1 = "ABC"
s2 = "XYZ"
f = open("data/test1.dat", "w")
pickle.dump(s1, f)
pickle.dump(s2, f)
f.close()

f = open("data/test1.dat", "r")
x1 = pickle.load(f)
x2 = pickle.load(f)
f.close()

class Foo:
    def display(self):
        print(self.x)
    def __init__(self, x0):
        self.x = x0

foo = Foo(66)
f = open("data/test2.dat", "w")
pickle.dump(foo, f)
f.close()

f = open("data/test2.dat", "r")
x = pickle.load(f)
x.display()
f.close()

1
