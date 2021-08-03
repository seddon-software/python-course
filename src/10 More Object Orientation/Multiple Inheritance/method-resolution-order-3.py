############################################################
#
#    mro
#
############################################################

O = object
class A(O): pass
class B(O): pass
class C(O): pass
class D(O): pass
class E(O): pass
# mro's of above classes are trivial

class K(A,B,C): pass
class L(D,B,E): pass
class M(D,A): pass
class Z(K,L,M): pass
# mro's of above classes are complicated

# mro(K) = KABC 
for clazz in K.mro():
    print(str(clazz))
print()

# mro(L) = LDBE
for clazz in L.mro():
    print(str(clazz))
print()

# mro(M) = MDA
for clazz in M.mro():
    print(str(clazz))
print()

# mro(Z) =
# Z         + merge(mro(K),mro(L),mro(M),KLM)
# Z         + merge(KABC  ,LDBE  ,MDA   ,KLM)
# ZK        + merge( ABC  ,LDBE  ,MDA   , LM)
#               skip ABC (A is in a tail)
# ZKL       + merge( ABC  , DBE  ,MDA   ,  M)
#  skip ABC (A is in a tail)
#  skip DBE (D is in a tail)
# ZKLM      + merge( ABC  , DBE  , DA   ,   )
#  skip ABC (A is in a tail)
# ZKLMD     + merge( ABC  ,  BE  ,  A   ,   )
# ZKLMDA    + merge(  BC  ,  BE  ,      ,   )
# ZKLMDAB   + merge(   C  ,   E  ,      ,   )
# ZKLMDABC  + merge(      ,   E  ,      ,   )
# ZKLMDABCE + merge(      ,      ,      ,   )

for clazz in Z.mro():
    print(str(clazz))

# mro would put C before D, but this contradicts mro(Z)
# hence this class is illegal
class Y(Z,C,D): pass
