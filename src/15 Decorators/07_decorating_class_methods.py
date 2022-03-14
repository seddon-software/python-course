'''
Decorating Class Methods
========================

This time a method is decorated.  Now consider
            m.addText("line 1")
this can be rewritten
            MyClass.addText(m, "line 1")

and after applying the trace decorator, this translates to
            trace(MyClass.addText)() with closure on fn=MyClass.addText, obj = m, value = "line 1"

Now trace(MyClass.addText) returns "enhance" and therefore we end up with (not forgetting the extra brackets):
            enhance() with closure on fn=MyClass.addText, obj = m, value = "line 1"

Thus we call enhance as
            enhance(obj=m, value="line 1")

and the function prints the trace
            calling addText('line 1')
before returning
            fn(obj, value) or MyClass.addText(m, "line 1")

Thus we get a trace before the original method is called.
'''

# the method is passed directly to the decorator, the object
# to the inner function
def trace(fn):
    def enhance(obj,value):
        print(f"calling {fn.__name__}('{value}')")
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
