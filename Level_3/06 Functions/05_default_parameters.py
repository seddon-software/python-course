############################################################
#
#    default parameters
#
############################################################

    
def display(a, b=10, c=100):
    print(f"a = {a:6.2f}, b = {b:6.2f}, c = {c:6.2f}")

display(a=19, b=-6.2, c=4.8)
display(b=-6.2, c=4.8, a=19 )
display(17)
display(17, 21)
display(17, c=0)
print(display.__defaults__)