############################################################
#
#    Variable Length Parameter Lists
#
############################################################

def f(x,y, **params):
    print('x,y:', x, y)
    print('params:', params)
    print(params['Dec'])
    

f(13,7, Jan=31, Feb=28, Dec=31)
summer = {'Jul':31, 'Aug':31, 'Sep':30}    
f(13,7, May=31, Jan=31, Feb=28, Dec=31, **summer)


