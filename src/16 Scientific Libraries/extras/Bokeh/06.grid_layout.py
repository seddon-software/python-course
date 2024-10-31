'''
Grid Layout
===========
Bokeh can produce multiple plots on a web page based around a grid layout.
'''

import bokeh.plotting as bp
import numpy as np

bp.output_file("html/grid-layout.html")

X = np.arange(0, 20, 2)
Y1 = 50-X**2
Y2 = X**3
Y3 = abs(X-5)
Y4 = X**2

fig1 = bp.figure(background_fill_color="#fafafa")
fig1.circle(X, Y1, size=12, alpha=0.8, color='red')

fig2 = bp.figure(background_fill_color="#fafafa")
fig2.triangle(X, Y2, size=12, alpha=0.8, color='green')

fig3 = bp.figure(background_fill_color="#fafafa")
fig3.square(X, Y3, size=12, alpha=0.8, color='blue')

fig4 = bp.figure(background_fill_color="#fafafa")
fig4.diamond(X, Y4, size=12, alpha=0.8, color='brown')

grid = bp.gridplot([[fig1, fig2], [fig3, fig4]], plot_width=250, plot_height=250)
bp.show(grid)
