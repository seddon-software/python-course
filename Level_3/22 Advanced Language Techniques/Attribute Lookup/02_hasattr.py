class MyImplemention:
    def f1(self): print("this is f1()")
    def f3(self): print("this is f3()")

x = MyImplemention()

if hasattr(x, "f1"): x.f1()
if hasattr(x, "f2"): x.f2()
if hasattr(x, "f3"): x.f3()

1