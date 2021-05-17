def trace(clazz):
    def inner():
        print("decorator called with", clazz)
        return clazz()
    return inner

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
a.f1()
a.f2()
a.f3()
a.f4()
