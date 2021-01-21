############################################################
#
#    Lone *
#
############################################################

def f(a, b, *, c, d):
    print(a, b, c, d)
    

# f("one", "two", "three", "four")        # c, d must be passed by name
f("one", "two", c="three", d="four")
f("one", b="two", c="three", d="four")
f(a="one", b="two", c="three", d="four")

