'''
Categories and Tooltips
=======================
When you don't want numerical values on an axis you can use categories (sting values).  In this example we use
a "vbar" to plot teams against points won in the Champions League.  We've also added some tooltips which you'll
see if you hover over the chart:
            tooltips=[("team:", "@x"),("points:", "@top")],

The "@x" and "@top" refer to the values passed to "vbar":
            fig.vbar(x=teams, top=points, width=0.9)
'''

import bokeh.plotting as bp
import numpy as np

teams = ['Juventus', 'Atletico Madrid', 'Leverkusen', 'Lokomotive Moscow']
points = [13, 7, 6, 3]

fig = bp.figure(x_range=teams,
              plot_height=250, 
              title="Champions League Table",
              tooltips=[("team:", "@x"),("points:", "@top")],
              toolbar_location=None, 
              tools="hover")

fig.vbar(x=teams, top=points, width=0.9)
fig.xgrid.grid_line_color = 'red'

bp.output_file("html/categories.html")
bp.show(fig)
