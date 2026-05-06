'''
Markers
=======

This example shows all possible markers that you can use with scatter plots
'''

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure("Markers")
ax = figure.add_subplot(1,1,1, projection='3d')

markers = {
        '.'  :  'point marker',
        ','  :  'pixel marker',
        'o'  :  'circle marker',
        'v'  :  'triangle_down marker',
        '^'  :  'triangle_up marker',
        '<'  :  'triangle_left marker',
        '>'  :  'triangle_right marker',
        '1'  :  'tri_down marker',
        '2'  :  'tri_up marker',
        '3'  :  'tri_left marker',
        '4'  :  'tri_right marker',
        's'  :  'square marker',
        'p'  :  'pentagon marker',
        '*'  :  'star marker',
        'h'  :  'hexagon1 marker',
        'H'  :  'hexagon2 marker',
        '+'  :  'plus marker',
        'x'  :  'x marker',
        'D'  :  'diamond marker',
        'd'  :  'thin_diamond marker',
        '|'  :  'vline marker',
        '_'  :  'hline marker',
        }
markers = list(markers.keys())

for i, marker in enumerate(markers):
    ax.scatter([i], [i], s = 100, marker=marker, color = np.random.rand(3))

plt.show()


