############################################################
#
#    object oriented plot
#
############################################################


import matplotlib.pyplot as plt

# object oriented interface uses axes 

ax = plt.subplot()      # create single figure with one axis
redCircles = "ro"
ax.plot([1,2,3,4], [1,4,9,16], redCircles)
ax.axis([0, 6, 0, 20])
ax.set_ylabel("squares")
plt.show()

