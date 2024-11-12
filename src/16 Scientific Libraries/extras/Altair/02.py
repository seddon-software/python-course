import altair as alt 
from vega_datasets import data 

# importing cars dataset 
# form vega_datasets provided by altair 
car_data  = data.cars() 
  
# making the simple histogram on Acceleration 
hist = alt.Chart(car_data).mark_bar().encode(x = 'Acceleration', 
                                             y = 'count()') 
# showing the histogram 
hist.show()

# render in browser
import os, webbrowser as wb
tempFile = "/tmp/chart.html"
hist.save(tempFile)
wb.open(tempFile)
os.system(f"rm {tempFile}")
