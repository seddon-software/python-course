############################################################
#
#    Lone *
#
############################################################

def f(a, b, *, c, d):
    print(a, b, c, d)
    

try:
    f("one", "two", "three", "four")        # c, d must be passed by name
except Exception as e:
    print(e)

f("one", "two", c="three", d="four")
f("one", b="two", c="three", d="four")
f(a="one", b="two", c="three", d="four")

