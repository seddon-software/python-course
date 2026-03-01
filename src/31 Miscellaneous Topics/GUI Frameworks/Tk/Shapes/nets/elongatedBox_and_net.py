import tkinter as tk
from tkinter import Canvas
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

import matplotlib.pyplot as plt

# Create 3D visualization
fig = plt.figure(figsize=(12, 5))

# 3D Box
ax1 = fig.add_subplot(121, projection='3d')

# Define vertices of an elongated box
vertices = np.array([
    [0, 0, 0],
    [3, 0, 0],
    [3, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [3, 0, 1],
    [3, 1, 1],
    [0, 1, 1]
])

# Define the 6 faces
faces = [
    [vertices[0], vertices[1], vertices[5], vertices[4]],  # bottom
    [vertices[2], vertices[3], vertices[7], vertices[6]],  # top
    [vertices[0], vertices[3], vertices[7], vertices[4]],  # left
    [vertices[1], vertices[2], vertices[6], vertices[5]],  # right
    [vertices[0], vertices[1], vertices[2], vertices[3]],  # front
    [vertices[4], vertices[5], vertices[6], vertices[7]]   # back
]

# Create 3D box
box = Poly3DCollection(faces, alpha=0.7, facecolor='cyan', edgecolor='black')
ax1.add_collection3d(box)

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 1)
ax1.set_zlim(0, 1)
ax1.set_title('3D Elongated Box')

# Net visualization
ax2 = fig.add_subplot(122)
ax2.set_xlim(-1, 8)
ax2.set_ylim(-1, 5)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title('Net of the Box')

# Draw net (unfolded box)
rects = [
    # Front face (3x1)
    plt.Rectangle((2, 2), 3, 1, edgecolor='black', facecolor='cyan', linewidth=2),
    # Back face (3x1)
    plt.Rectangle((2, 0), 3, 1, edgecolor='black', facecolor='lightblue', linewidth=2),
    # Left face (1x1)
    plt.Rectangle((1, 2), 1, 1, edgecolor='black', facecolor='lightgreen', linewidth=2),
    # Right face (1x1)
    plt.Rectangle((5, 2), 1, 1, edgecolor='black', facecolor='lightgreen', linewidth=2),
    # Top face (3x1)
    plt.Rectangle((2, 3), 3, 1, edgecolor='black', facecolor='lightyellow', linewidth=2),
    # Bottom face (3x1)
    plt.Rectangle((2, 1), 3, 1, edgecolor='black', facecolor='lightyellow', linewidth=2),
]

for rect in rects:
    ax2.add_patch(rect)

plt.tight_layout()
plt.show()