import dis

def f():
    data = list(range(10))
    for x in data:
        yield x
    return

g = f()
next(g)

#print(dir(g))
print(g.__class__.__dict__)
dis.dis(g.__iter__)
#print(g.__next__)
#dis.dis(f)
