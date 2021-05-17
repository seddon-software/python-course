import numpy as np
from numpy import array, dot
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import sqrt


def update_plot(frame, data, sc):
    sc._offsets3d = data[frame]
    return sc

def main():
    matplotlib.use('TkAgg')
    frames = 2000
    dimensions = 3
    particles = 20
    data = np.ones(frames * dimensions * particles)
    data = data.reshape(frames, dimensions, particles)

    for particle in range(particles):
        for dimension in [0, 1, 2]:
            for frame in range(frames): 
                # build some snake like movement for the points
                if dimension == 0: data[frame][dimension][particle] = particle * np.sin(frame/40.0) * 10 * np.sin(particle/4.0)
                if dimension == 1: data[frame][dimension][particle] = particle * np.sin(frame/20.0) * 10
                if dimension == 2: data[frame][dimension][particle] = particle * np.cos(frame/10.0) * 10
                
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d([-250.0, 250.0])
    ax.set_ylim3d([-250.0, 250.0])
    ax.set_zlim3d([-250.0, 250.0])
    ax.set_autoscale_on(False)

    ix, iy, iz = data[0]
    sc = ax.scatter(ix, iy, iz, s=100.0, c='red', marker='d')
    def init():
        return ax
    ani = FuncAnimation(fig, update_plot, frames=frames, fargs=(data,sc), interval=100)
    plt.show()


main()
    