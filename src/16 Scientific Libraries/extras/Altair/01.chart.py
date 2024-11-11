'''
Create an altair chart.  Altair needs to be rendered, usually in a web page, so we save the chart in a file
and open a browser to view the chart
'''

# import altair with an abbreviated alias
import altair as alt
import os, webbrowser as wb

# load a sample dataset as a pandas DataFrame
from vega_datasets import data
cars = data.cars()

# make the chart
chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive().properties(
    width=1200,
    height=450
)

tempFile = "/tmp/chart.html"
chart.save(tempFile)
wb.open(tempFile)
os.system(f"rm {tempFile}")
