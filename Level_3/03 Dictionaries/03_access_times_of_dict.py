import sys, timeit

'''
Create a dictionary of various sizes and then time accessing an element of the dictionary
'''

def setupDictionary(n):
    d = {}
    for i in range(n):
        key = f"key{i}"
        value = f"value{i}"
        d[key] = value
    return d

d = {}
def timeDictionaryAccess(N):
    global d
    d = setupDictionary(N)
    statement = f"""v = d['key{N//2}']"""
    print(N, timeit.timeit(statement, globals=globals()))

timeDictionaryAccess(10)
timeDictionaryAccess(100)
timeDictionaryAccess(1000)
timeDictionaryAccess(10000)
timeDictionaryAccess(100000)
timeDictionaryAccess(1000000)
timeDictionaryAccess(10000000)
    
