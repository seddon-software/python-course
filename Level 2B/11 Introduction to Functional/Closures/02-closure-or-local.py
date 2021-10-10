def scope(fn):
    closure = fn.__closure__
    if closure is None: return ""
    for c in closure:
        print("closure: {:46s}{}".format(str(c.cell_contents), c))
    print("locals:", fn.__code__.co_varnames)

def f1():
    x1 = [10, 20, 30, 40]     # mutable
    x2 = {}                   # mutable
    y1 = 11                   # immutable
    y2 = None                 # immutable
    y3 = "hello"              # immutable
    def f2():
        # note y1 and y2 are locals, not closures        
        x1[0] = 99
        x2['red'] = 255
        y1 = 10
        y2 = y3
    f2()
    scope(f2)

f1()
