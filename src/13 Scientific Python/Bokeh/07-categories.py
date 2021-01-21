import bokeh.plotting as bp
import numpy as np
from bokeh.palettes import Spectral4
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
bp.output_file("html/categories.html")

teams = ['Juventus', 'Atletico Madrid', 'Leverkusen', 'Lokomotive Moscow']
points = [13, 7, 6, 3]
fig = bp.figure(x_range=teams, 
              plot_height=250, 
              title="Champions League Table",
              tooltips=TOOLTIPS,
              toolbar_location=None, 
              tools="")

fig.vbar(x=teams, top=points, width=0.9)

fig.xgrid.grid_line_color = 'red'
fig.y_range.start = 0

bp.show(fig)
