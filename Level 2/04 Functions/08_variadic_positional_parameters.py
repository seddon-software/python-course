############################################################
#
#    Variable Length Parameter Lists
#
############################################################

def  f(*args):
    print('args:', args)
    
a = (3,4,7,8)
b = [3,4,7,8]

f(1,3,4,7,8,9)      # pass multiple args
f(1,a,9)    # pass int, tuple, int
f(1,b,9)    # pass int, list, int
f(1,*a)     # treat tuple as multiple args
f(1,*b)     # treat list as multiple args
