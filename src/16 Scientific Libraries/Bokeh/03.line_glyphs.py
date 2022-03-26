'''
Line Glyphs
===========
This time we are plotting a sinusoidal graph from Numpy arrays.
'''

#from bokeh.plotting import figure, output_file, show
import bokeh.plotting as bp
import numpy as np

bp.output_file("html/line.html")

fig = bp.figure(plot_width=800, plot_height=600)

X = np.arange(-5, 5, 0.01)
Y = np.sin(X)
fig.line(X, Y, line_width=2)

bp.show(fig)
