import matplotlib.pyplot as plt
import numpy as np
'''
ax.annotate('Something', xy=(x[0], y[0]), xytext=(-20,20), 
            textcoords='offset points', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5', 
                            color='red'))
'''
PHONE="07470 378260"
ax = plt.subplot()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.rc('font', size=16)
A = [2,3]
B = [2,3]

# ax.scatter(A, B, c="red" )
X = np.linspace(0, 1, 4)
y = np.linspace(0, 1, 4)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.01)

def write(x, y):
    ax.text(x, y, PHONE, transform=ax.transAxes, fontsize=14, fontweight=0.1,
            verticalalignment='top', bbox=props)

for x in np.linspace(0.35, 0.35, 1):
    for y in np.linspace(0.1, 0.9, 2):
        write(x, y)
        # ax.annotate(text=PHONE, xy=(x, y), 
        #             bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3))
#plt.axes("off")
plt.show()

