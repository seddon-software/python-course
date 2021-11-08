############################################################
#
#    mtlab type plot
#
############################################################


# matplotlib.pyplot is a state-based interface to matplotlib.
# It provides a MATLAB-like way of plotting.
# pyplot is mainly intended for interactive plots and simple plots
import matplotlib.pyplot as plt
import os
os.system("clear")


redCircles = "ro"
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], redCircles)
plt.axis([0, 6, 0, 20])
plt.ylabel("squares")
plt.show()

1
