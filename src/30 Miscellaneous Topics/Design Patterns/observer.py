############################################################
#
#    Observer (Pub/Sub)
#
############################################################

from abc import ABCMeta, abstractmethod

class IObserver(object):
    @abstractmethod
    def Callback(self, state): pass

class ISubject(object):
    @abstractmethod
    def Register(self, observer): pass 

    @abstractmethod
    def UnRegister(self, observer): pass 

    @abstractmethod
    def Notify(self): pass


class ConcreteSubject(ISubject):
    def __init__(self):
        self.observers = list()
        self.state = 0.0

    def ChangeState(self, state):
        if(state != self.state):
            self.state = state
            self.Notify()
        
        
    def Register(self, observer):
        self.observers.append(observer)
    
    def UnRegister(self, thisObserver):
        for observer in self.observers:
            if(thisObserver == observer):
                self.observers.remove(thisObserver)
    
    def Notify(self):
        for observer in self.observers:        
            observer.Callback(self.state);

class ConcreteObserver(IObserver):
    def __init__(self, id):
        self.id = id
         
    def Callback(self, state):
        print("observer", self.id, "sees state change to:", state)


##### main

publisher = ConcreteSubject()
subscriber1 = ConcreteObserver("1")
subscriber2 = ConcreteObserver("2")
subscriber3 = ConcreteObserver("3")
    
publisher.Register(subscriber1)
publisher.Register(subscriber2)
publisher.Register(subscriber3)

publisher.ChangeState(3.3)
publisher.ChangeState(3.5)
publisher.ChangeState(3.5)
publisher.ChangeState(3.7)

publisher.UnRegister(subscriber2)
publisher.ChangeState(3.9)
