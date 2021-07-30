############################################################
#
#    mro
#
############################################################

class MyMetaclass(type):
    # override the usual MRO defined by inheritance
    def mro(cls):
        return (cls, B, object) # note that A is missing
    
class A(object): pass
class B(A): pass
class C1(B): pass
class C2(B, metaclass=MyMetaclass): pass

# inheritance hierarchy appears to be:
#     object
#        |
#        A
#        |
#        B
#        |
#     -------
#     |     |
#     C1    C2

# but C2 uses a metaclass to override this
 
# print the inheritance mro for C1 (as expected)
print("mro for C1: ", C1.__mro__)

# print the inheritance mro for C2 (note that it has been totally cahanged)
print("mro for C2: ", C2.__mro__)

