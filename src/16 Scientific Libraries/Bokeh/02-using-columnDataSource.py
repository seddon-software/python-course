import bokeh.plotting as bp

data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

bp.output_file("html/using-columnDataSource.html")
source = bp.ColumnDataSource(data=data)

fig = bp.figure(plot_width=800, plot_height=600)
fig.circle(x='x_values', y='y_values', source=source, radius=0.1)
bp.show(fig)

