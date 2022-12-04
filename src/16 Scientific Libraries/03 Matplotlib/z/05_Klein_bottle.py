import mpl_toolkits.mplot3d.axes3d as axes3d
import matplotlib.pyplot as plt
import numpy as np

cos = np.cos
sin = np.sin
sqrt = np.sqrt
pi = np.pi

def surf(u, v):
    """
    http://paulbourke.net/geometry/klein/
    """
    half = (0 <= u) & (u < pi)
    r = 4*(1 - cos(u)/2)
    x = 6*cos(u)*(1 + sin(u)) + r*cos(v + pi)
    x[half] = (
        (6*cos(u)*(1 + sin(u)) + r*cos(u)*cos(v))[half])
    y = 16 * sin(u)
    y[half] = (16*sin(u) + r*sin(u)*cos(v))[half]
    z = r * sin(v)
    return x, y, z

u, v = np.linspace(0, 2*pi, 40), np.linspace(0, 2*pi, 40)
ux, vx =  np.meshgrid(u,v)
x, y, z = surf(ux, vx)

fig = plt.figure()
ax = fig.gca(projection = '3d')
plot = ax.plot_surface(x, y, z, rstride = 1, cstride = 1, cmap = plt.get_cmap('terrain'),
                       linewidth = 0, antialiased = False)

plt.show()
