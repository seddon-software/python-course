tab = '\t'
class Base(object):
    def say(self, indent = 0):
        print(f'{tab*indent}Base')
class ChildA(Base):
    def say(self, indent = 0):
        print(f'{tab*indent}ChildA')
        super(ChildA, self).say(indent+1)
class ChildB(Base):
    def say(self, indent = 0):
        print(f'{tab*indent}ChildB')
        super(ChildB, self).say(indent+1)
class ChildC(ChildA, ChildB):
    def say(self, indent = 0):
        print(f'{tab*indent}ChildC')
        super(ChildC, self).say(1)
        
obj = ChildC()
# use super to call methods throughout the MRO
obj.say()



