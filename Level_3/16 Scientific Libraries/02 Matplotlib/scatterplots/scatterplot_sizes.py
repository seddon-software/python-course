import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure()
ax = figure.add_subplot(1,1,1)



x = [0,2,4,6,8,10];
y = np.zeros(len(x));
s = [20*2**n for n in range(len(x))];
print(x)
print(y)
print(s)
ax.scatter(x,y,s=s);
plt.show()
