import tkinter as tk
from tkinter import Canvas
import math

class PyramidVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pyramid and Net Visualization")
        self.root.geometry("1000x600")
        
        self.canvas = Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.draw_pyramid()
        self.draw_net()
    
    def draw_pyramid(self):
        """Draw a 3D pyramid"""
        offset_x, offset_y = 150, 250
        
        # Pyramid base vertices
        base_size = 100
        base = [
            (offset_x - base_size, offset_y),
            (offset_x + base_size, offset_y),
            (offset_x + base_size, offset_y + base_size),
            (offset_x - base_size, offset_y + base_size)
        ]
        
        # Apex
        apex = (offset_x, offset_y - 150)
        
        # Draw base (square)
        self.canvas.create_polygon(base[0], base[1], base[2], base[3], 
                                    fill="lightblue", outline="black", width=2)
        
        # Draw triangular faces
        self.canvas.create_polygon(base[0], base[1], apex, 
                                    fill="lightcoral", outline="black", width=2)
        self.canvas.create_polygon(base[1], base[2], apex, 
                                    fill="lightyellow", outline="black", width=2)
        self.canvas.create_polygon(base[2], base[3], apex, 
                                    fill="lightgreen", outline="black", width=2)
        self.canvas.create_polygon(base[3], base[0], apex, 
                                    fill="plum", outline="black", width=2)
        
        # Label
        self.canvas.create_text(150, 450, text="3D Pyramid", font=("Arial", 14, "bold"))
    
    def draw_net(self):
        """Draw the net of a pyramid"""
        offset_x, offset_y = 700, 250
        base_size = 50
        
        # Square base in center
        base_x = offset_x
        base_y = offset_y
        square = [
            (base_x - base_size, base_y - base_size),
            (base_x + base_size, base_y - base_size),
            (base_x + base_size, base_y + base_size),
            (base_x - base_size, base_y + base_size)
        ]
        
        self.canvas.create_polygon(*square, fill="lightblue", outline="black", width=2)
        
        # Calculate triangle height
        triangle_height = int(base_size * math.sqrt(3))
        
        # Top triangle
        top_tri = [
            (base_x - base_size, base_y - base_size),
            (base_x + base_size, base_y - base_size),
            (base_x, base_y - base_size - triangle_height)
        ]
        self.canvas.create_polygon(*top_tri, fill="lightcoral", outline="black", width=2)
        
        # Right triangle
        right_tri = [
            (base_x + base_size, base_y - base_size),
            (base_x + base_size, base_y + base_size),
            (base_x + base_size + triangle_height, base_y)
        ]
        self.canvas.create_polygon(*right_tri, fill="lightyellow", outline="black", width=2)
        
        # Bottom triangle
        bottom_tri = [
            (base_x + base_size, base_y + base_size),
            (base_x - base_size, base_y + base_size),
            (base_x, base_y + base_size + triangle_height)
        ]
        self.canvas.create_polygon(*bottom_tri, fill="lightgreen", outline="black", width=2)
        
        # Left triangle
        left_tri = [
            (base_x - base_size, base_y + base_size),
            (base_x - base_size, base_y - base_size),
            (base_x - base_size - triangle_height, base_y)
        ]
        self.canvas.create_polygon(*left_tri, fill="plum", outline="black", width=2)
        
        # Label
        self.canvas.create_text(700, 450, text="Pyramid Net", font=("Arial", 14, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = PyramidVisualizer(root)
    root.mainloop()