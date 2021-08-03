############################################################
#
#    Command Pattern
#
############################################################

from abc import ABCMeta, abstractmethod

class HeatingSystem(object):
    def __init__(self, name):
        self.name = name
        
    def turn_on(self): print("turn_on:" + self.name, end=' ')
    def turn_off(self): print("turn_off:" + self.name, end=' ')
    def service(self): print("service:" + self.name, end=' ')

######
### hierarchy
#
#                         Command
#                           ^
#                           |
#                       CommandAdapter
#
#             ______________=_____________
#             =             =             =
#           HeatingOn     HeatingOff     Service   (CommandAdapter objects)
#####

class Command(object, metaclass=ABCMeta):
    @abstractmethod
    def execute(self): pass

# bound methods are bound to an instance
# unbound methods are bound to a class

class CommandAdapter(Command):
    def __init__(self, callback): 
        self.callback = callback    # this is a bound method

    def execute(self):
        self.callback()             # call bound method
        
           

#####

class Time(object):
    def __init__(self, t):
        self.ticks = t


class TimerController(object):
    def __init__(self):
        self.clock = 0
        self.events = list()
        self.times = list()

    def set(self, when, what):
        self.events.append(what)
        self.times.append(when)

    def check_for_events(self, t):
        print(); print(t, ": ", end=' ')
        self.clock = t
        self.fire_events()
        
    def fire_events(self):
        for i in range(len(self.events) - 1):
            if(self.times[i] == self.clock): 
                self.events[i].execute()


##### main

systemA = HeatingSystem("A")
systemB = HeatingSystem("B")
controller = TimerController()

onA      = CommandAdapter(systemA.turn_on)
offA     = CommandAdapter(systemA.turn_off)
serviceA = CommandAdapter(systemA.service)
onB      = CommandAdapter(systemB.turn_on)
offB     = CommandAdapter(systemB.turn_off)
serviceB = CommandAdapter(systemB.service)

controller.set( 4, onA)
controller.set( 8, offA)
controller.set(10, serviceA)
controller.set( 2, onB)
controller.set( 3, offB)
controller.set( 7, onB)
controller.set( 8, offB)
controller.set(11, serviceB)

print("start of simulation")

for t in range(1, 13):
    controller.check_for_events(t)

print(); print("end of simulation")



