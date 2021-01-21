class MyInterface:
	def __init__(self):
		if issubclass(MyInterface, self.__class__):
			raise Exception("you cannot instantiate an interface")
	
	def f1(self): raise Exception("not implemented")
	def f2(self): raise Exception("not implemented")
	def f3(self): raise Exception("not implemented")

class MyImplemention(MyInterface):
    def f1(self): print("this is f1()")
    def f2(self): print("this is f2()")
    def f3(self): print("this is f3()")

x = MyImplemention()
x.f1()
x.f2()
x.f3()

try:
	y = MyInterface()
except Exception as e:
	print(e)
