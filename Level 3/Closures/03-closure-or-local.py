def scope(fn):
    closure = fn.__closure__
    if closure is None:
        return ""
    for c in closure:
        print(f"closure: {str(c.cell_contents):25s}{c}")
    print(f"locals not available for closure: {fn.__code__.co_varnames}")
    print(f"variables available on closure: {fn.__code__.co_freevars}")


def main():
    x1 = [10, 20, 30, 40]     # mutable
    x2 = {}                   # mutable
    y1 = 11                   # immutable
    y2 = None                 # immutable
    y3 = "hello"              # immutable

    def f():
        # note x1 and x2 are mutable and can be modified in f(), hence closures
        # note y1 and y2 are local to f(), and not closures on main()
        # y3 is not defined in this function, hence closure on main()
        x1[0] = 99
        x2['red'] = 255
        y1 = 10
        y2 = y3
    f()
    scope(f)


main()
