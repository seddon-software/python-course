#from bokeh.plotting import figure, output_file, show
import bokeh.plotting as bp
import numpy as np


    
bp.output_file("html/vbar.html")

fig = bp.figure(plot_width=800, plot_height=600)

X = range(-5, 6)
Y = [x**2 for x in X]
fig.vbar(x=X, width=0.5, bottom=0, top=Y, color="firebrick")

bp.show(fig)
