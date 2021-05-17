############################################################
#
#    mro
#
############################################################


class A(object):
    def f(self):
        print("A;f()")

class B(A):
    pass

class C(A):
    def f(self):
        print("C;f()")

class D(B,C):
    pass


for clazz in D.mro():
    print(str(clazz))
    

