############################################################
#
#    mypackage.py
#
############################################################

def trace():
    pass
x = 200
    
symbols = dict(globals())
for key, value in symbols.items():
    print("{0:16} {1}".format(key, value))
    



