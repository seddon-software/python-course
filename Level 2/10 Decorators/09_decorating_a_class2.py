def trace(clazz):
    class X:
        def __init__(self, *args, **kwargs):
            self.clazz = clazz
            
#         def __getattribute__(self,s):
#             print(s)
#             o = self.clazz
#             z = o.__dict__[s]
#             z()
        def __getattr__(self, name):
                print("__getattr__", self, self.clazz)
#                self.__dict__[name] = None # used to avoid recursion
                fn = self.clazz.__dict__[name]
                print(fn)
                fn(self)
    x = X()
    return X
#     def inner():
#         print("decorator called with", clazz)
#         return clazz()
#     return inner

@trace
class A:
    def f1(self):
        print('f1')
    def f2(self):
        print('f2')
    def f3(self):
        print('f3')
    def f4(self):
        print('f4')

a = A() # a = trace(A)
print(a)
a.f1()
a.f2()
a.f3()
a.f4()
