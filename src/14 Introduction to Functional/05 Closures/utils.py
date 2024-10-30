'''
This function is used in other examples to display closures
'''
def displayClosures(fn):
    if fn.__closure__:
        closures = zip(fn.__closure__, fn.__code__.co_freevars)
        if closures:    # check there are entries in the closure
            for cl, fv in closures:
                print(f"closure for {fn.__name__}[0x{id(fn):x}]: {fv} = {cl.cell_contents}")
        else:
            print(f"closure for {fn.__name__}: empty")
        #print()       
    else:
        print(f"closure for {fn.__name__}: empty")
