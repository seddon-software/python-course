############################################################
#
#    ModuleB
#
############################################################

from package1.package3 import ModuleD as D
class B:
    def f(self):
        print("this is B.f() ...")
    def g(self):
        print("this is B.g() ...")
    def h(self):
        d = D.D()
        d.f()
        print("this is B.h() ...")

    
    