import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

import matplotlib.pyplot as plt

def draw_prism_and_net():
    fig = plt.figure(figsize=(14, 6))
    
    # 3D Prism
    ax1 = fig.add_subplot(121, projection='3d')
    
    # Define vertices of a triangular prism
    vertices = np.array([
        [0, 0, 0],      # 0
        [2, 0, 0],      # 1
        [1, 1.7, 0],    # 2
        [0, 0, 2],      # 3
        [2, 0, 2],      # 4
        [1, 1.7, 2]     # 5
    ])
    
    # Define faces with colors
    faces = [
        ([vertices[0], vertices[1], vertices[4], vertices[3]], 'red'),       # front
        ([vertices[1], vertices[2], vertices[5], vertices[4]], 'blue'),      # right
        ([vertices[2], vertices[0], vertices[3], vertices[5]], 'green'),     # left
        ([vertices[0], vertices[1], vertices[2]], 'yellow'),                 # bottom
        ([vertices[3], vertices[4], vertices[5]], 'purple')                  # top
    ]
    
    for face, color in faces:
        poly = Poly3DCollection([face], alpha=0.7, facecolors=color, edgecolors='black', linewidths=1.5)
        ax1.add_collection3d(poly)
    
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_xlim([-1, 3])
    ax1.set_ylim([-1, 3])
    ax1.set_zlim([-1, 3])
    ax1.set_title('3D Triangular Prism')
    
    # Net (2D unfolding)
    ax2 = fig.add_subplot(122)
    
    # Define net pieces in 2D (connected)
    colors_net = ['yellow', 'red', 'blue', 'green', 'purple']
    
    # Bottom triangle
    bottom = np.array([[0, 0], [2, 0], [1, 1.7]])
    ax2.fill(*bottom.T, color=colors_net[0], edgecolor='black', linewidth=2)
    
    # Front rectangle attached to bottom edge (0,0)-(2,0)
    front = np.array([[0, 0], [2, 0], [2, -2], [0, -2]])
    ax2.fill(*front.T, color=colors_net[1], edgecolor='black', linewidth=2)
    
    # Right rectangle attached to bottom edge (2,0)-(1,1.7)
    right = np.array([[2, 0], [1, 1.7], [2, 3.7], [3, 2]])
    ax2.fill(*right.T, color=colors_net[2], edgecolor='black', linewidth=2)
    
    # Left rectangle attached to bottom edge (1,1.7)-(0,0)
    left = np.array([[0, 0], [1, 1.7], [-1, 3.7], [-2, 2]])
    ax2.fill(*left.T, color=colors_net[3], edgecolor='black', linewidth=2)
    
    # Top triangle attached to front rectangle
    top = np.array([[0, -2], [2, -2], [1, -3.7]])
    ax2.fill(*top.T, color=colors_net[4], edgecolor='black', linewidth=2)
    
    ax2.set_xlim([-3, 4])
    ax2.set_ylim([-5, 5])
    ax2.set_aspect('equal')
    ax2.set_title('Unfolded Net (Connected)')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_prism_and_net()