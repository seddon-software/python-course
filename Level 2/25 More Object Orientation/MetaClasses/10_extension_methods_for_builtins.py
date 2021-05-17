############################################################
#
#    binding methods to built-ins
#
############################################################

# You can't bind extra methods to builtin classes or classes
# defined in the C language.  However you can inherit from
# builtins and add methods to the derived class.

class UpperList(list):
    pass

def to_upper(self):
    for index, item in enumerate(self):
        self[index] = item.upper()

UpperList.to_upper = to_upper

mylist = UpperList(['i','g','o','r'])
mylist.to_upper()
print(mylist)

1