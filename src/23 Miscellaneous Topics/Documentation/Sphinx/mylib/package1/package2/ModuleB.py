############################################################
#
#    ModuleB
#
############################################################

'''
This is ModuleB
It imports ModuleD
'''

from package1.package3 import ModuleD as D
class B:
    '''class B contains 3 methods and calls a classD object'''
    def f(self):
        print("this is B.f() ...")
    def g(self):
        print("this is B.g() ...")
    def h(self):
        d = D.D()
        d.f()
        print("this is B.h() ...")

    
    