import bokeh.plotting as bp
import numpy as np
    
bp.output_file("html/vbar-stack.html")

fig = bp.figure(plot_width=800, plot_height=600)

Y = range(-4, 5)
X1 = [y**2 for y in Y]
X2 = [y for y in Y]
source = bp.ColumnDataSource(data={'y':Y, 'x1':X1, 'x2':X2})
fig.vbar_stack(['x1', 'x2'], x='y', width=0.9, color=['blue', 'red'], source=source)

bp.show(fig)

