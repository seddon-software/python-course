'''
Plot using Bokeh
================
Bokeh is a web based presentation program.  Bokeh creates an HTML file; you can display this file in a browser
using:
            output_notebook()
            show(p)
'''

import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.transform import factor_cmap, factor_mark
from bokeh.io import output_notebook

output_file("bokeh.html")
iris_df = pd.read_csv("data/iris.csv")
flowers = iris_df
SPECIES = ['setosa', 'versicolor', 'virginica']
MARKERS = ['hex', 'circle_x', 'triangle']

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Sepal Width'

p.scatter("petal_length", "sepal_width", 
          source=iris_df, 
          fill_alpha=0.4, 
          size=12,
          marker=factor_mark('species', MARKERS, SPECIES),
          color=factor_cmap('species', 'Category10_3', SPECIES))
output_notebook()
show(p)

