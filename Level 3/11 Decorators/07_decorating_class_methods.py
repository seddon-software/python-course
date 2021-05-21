############################################################
#
#    decorators
#
############################################################

# the method is passed directly to the decorator, the object
# to the inner function
def trace(fn):
    def enhance(obj,value):
        print("calling {0}('{1}')".format(fn.__name__, value))
        return fn(obj, value)
    return enhance
    
    
class MyClass(object):
    def __init__(self):
        self.text = ""
        
    @trace
    def addText(self, text):
        self.text += text + "\n"
    
    def addText2(self, text):
        self.text += text + "\n"
    
    def display(self):
        print(self.text)


m = MyClass()
m.addText("line 1")
m.addText("line 2")
m.addText("line 3")
m.addText("line 4")
m.addText("line 5")
m.display()

# functional version
trace(MyClass.addText2)(m, "line 6")
m.display()

1
