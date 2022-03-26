'''
Using a ColumnDataSource
========================
The ColumnDataSource is a fundamental data structure of Bokeh. Most plots, data tables, etc. will be driven by a 
ColumnDataSource.  The data source can be a Pandas dataframe, Numpy arrays or as we've used here, a Python dict.

In the example we print a plot of circles using the 'x_values' and 'y_values' from the data source.
'''

import bokeh.plotting as bp

data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

bp.output_file("html/using-columnDataSource.html")
source = bp.ColumnDataSource(data=data)

fig = bp.figure(plot_width=800, plot_height=600)
fig.circle(x='x_values', y='y_values', source=source, radius=0.1)
bp.show(fig)

