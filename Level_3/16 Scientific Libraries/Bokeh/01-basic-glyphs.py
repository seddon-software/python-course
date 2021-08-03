import bokeh.plotting as bp

X = [1, 2, 3, 4, 5]
Y = [14, 11, 8, 5, 2]

bp.output_file("html/basic-glyphs.html")
# bp.output_notebook()
fig = bp.figure(plot_width=800, plot_height=600)
fig.circle(x=X, y=Y, radius=0.1)

X = [x+1 for x in X]
Y = [y-1 for y in Y]
fig.square(x=X, y=Y, size=20, color="olive", alpha=0.5)

X = [x+1 for x in X]
Y = [y-1 for y in Y]

fig.diamond(x=X, y=Y, size=40, angle=-45.0, color="pink")
bp.show(fig)
