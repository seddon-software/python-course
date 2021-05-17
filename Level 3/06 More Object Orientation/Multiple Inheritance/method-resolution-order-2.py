############################################################
#
#    mro
#
############################################################

o = object
class a(o): 
    def f(self): print("a", end=' '); super(a,self).f()
class b(o): 
    def f(self): print("b", end=' '); super(b,self).f()
class c(o): 
    def f(self): print("c", end=' ')
class x(a): 
    def f(self): print("x", end=' '); super(x,self).f()
class y(a): 
    def f(self): print("y", end=' '); super(y,self).f()
class z(x,b,y,c): 
    def f(self): print("z", end=' '); super(z,self).f()


for clazz in x.mro():
    print(str(clazz))
print()

for clazz in y.mro():
    print(str(clazz))
print()

# mro(z) =
# z       + merge(mro(x)+mro(b)+mro(y)+mro(c)+xbyc)
# z       + merge(xao   +bo    +yao   +co    +xbyc)
# zx      + merge( ao   +bo    +yao   +co    + byc)
# zxb     + merge( ao   + o    +yao   +co    +  yc)
# zxby    + merge( ao   + o    + ao   +co    +   c)
# zxbya   + merge(  o   + o    +  o   +co    +   c)
# zxbyac  + merge(  o   + o    +  o   + o    +    )
# zxbyaco + merge(      +      +      +      +    )
# zxbyaco

# each list is defined as HTTTTT where H = head and T = tail
# when merging you look for a head that doesn't appear in the
# tail of any other list
# note that some merges are impossible and class won't compile

for clazz in z.mro():
    print(str(clazz))
print(z.__mro__)    
t = z()
t.f()

