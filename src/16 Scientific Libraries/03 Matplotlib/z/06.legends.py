import matplotlib.pyplot as plt 
# data to display on plots 
x = [3, 1, 3] 
y = [3, 2, 1] 
plt.plot(x, y)
plt.plot(y, x)
# Adding the legends
plt.legend(["blue", "orange"])
plt.show()