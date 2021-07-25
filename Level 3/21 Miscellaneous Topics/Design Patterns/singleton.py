class Singleton:
    theInstance = None
    @classmethod
    def Create(cls):
        if Singleton.theInstance == None:
            Singleton.theInstance = Singleton()
        return Singleton.theInstance
    
    def whatsMyId(self):
        print(id(self))
        

x1 = Singleton.Create()
x2 = Singleton.Create()
x3 = Singleton.Create()
x4 = Singleton.Create()


x1.whatsMyId()
x2.whatsMyId()
x3.whatsMyId()
x4.whatsMyId()



1