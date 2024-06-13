def displayClosures(fn):
    if fn.__closure__:
        closures = zip(fn.__closure__, fn.__code__.co_freevars)
#        next(closures)      # skip the closure cell on the function name (always the first)
        if closures:    # check there are other entries in the closure
            for c, f in closures:
                print(f"closure for {fn.__name__}: {f} = {c.cell_contents}")
        else:
            print(f"closure for {fn.__name__}: empty")        
    else:
        print(f"closure for {fn.__name__}: empty")
