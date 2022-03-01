'''
Dictionary order is guaranteed to be insertion order. This behavior was an implementation detail of 
CPython from 3.6 (this new behavior became guaranteed in Python 3.7)
'''

d = {'one':1, 'two':2,'three':3}
d['four'] = 4
d.update({'five':5, 'six':6})
print(d)

