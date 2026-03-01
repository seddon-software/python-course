import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

import matplotlib.pyplot as plt

def draw_cylinder_3d():
    fig = plt.figure(figsize=(12, 5))
    
    # 3D Cylinder
    ax1 = fig.add_subplot(121, projection='3d')
    
    height = 2
    radius = 1
    theta = np.linspace(0, 2*np.pi, 50)
    z = np.linspace(0, height, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)
    
    ax1.plot_surface(x_grid, y_grid, z_grid, alpha=0.7, cmap='viridis')
    
    # Top and bottom circles
    theta_circle = np.linspace(0, 2*np.pi, 50)
    x_circle = radius * np.cos(theta_circle)
    y_circle = radius * np.sin(theta_circle)
    ax1.plot(x_circle, y_circle, height, 'b-', linewidth=2)
    ax1.plot(x_circle, y_circle, 0, 'b-', linewidth=2)
    
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('3D Cylinder')
    
    # Cylinder Net
    ax2 = fig.add_subplot(122)
    
    # Rectangle (lateral surface)
    circumference = 2 * np.pi * radius
    rect = plt.Rectangle((0, 0), circumference, height, fill=False, edgecolor='blue', linewidth=2)
    ax2.add_patch(rect)
    
    # Top circle
    circle_top = plt.Circle((circumference/2, height + radius + 0.3), radius, fill=False, edgecolor='red', linewidth=2)
    ax2.add_patch(circle_top)
    
    # Bottom circle
    circle_bottom = plt.Circle((circumference/2, -radius - 0.3), radius, fill=False, edgecolor='green', linewidth=2)
    ax2.add_patch(circle_bottom)
    
    ax2.set_xlim(-1, circumference + 1)
    ax2.set_ylim(-3, height + 3)
    ax2.set_aspect('equal')
    ax2.set_title('Cylinder Net')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    draw_cylinder_3d()