############################################################
#
#    slicing
#
############################################################

colors = ["red", "blue", "green", "white", "black"] 
print(colors[2])        # actually the third item
print(colors[-1])       # counting backwards (the last item)
print(colors[1:3])      # items 1 and 2
print(colors[1:])       # items 1 to last
print(colors[-3:-1])    # items third to last to last, but excluding last 
print(colors[4:1:-1])   # items 4, 3 and 2, working backwards
colors[2:4] = ("purple", "cyan") # change items 2 and 3
print(colors[0:])       # items 0 to end
print(colors[:])        # same
print(colors)           # same again

