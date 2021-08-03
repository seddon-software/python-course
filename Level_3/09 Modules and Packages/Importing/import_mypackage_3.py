# modules can be loaded at runtime by name (string)

# use this method if you don't know which module 
# to load at compile time
import sys
sys.path.append("mylib")

mp = __import__("mypackage")

mp.f1()
mp.f2()
mp.f3()
mp.f4()


1


