# any class with __len__ and __getitem__ is iterable
 
class Foo(object):
    def __len__(self):
        return 10

    def __getitem__(self, i):
        if i > len(self):
            raise IndexError
        return i

for i in Foo():
    print(i) 
    