'''
       yield           variety  year           site
0    27.00000         Manchuria  1930           maxT
1    48.86667         Manchuria  1931           maxT
2    27.43334         Manchuria  1932           maxT
3    39.93333         Manchuria  1933           maxT
4    27.00000         Manchuria  1930           minT
5    48.86667         Manchuria  1931           minT
6    27.43334         Manchuria  1932           minT
7    39.93333         Manchuria  1933           minT
'''

import altair as alt

import polars as pl
import pandas as pd

df = pd.read_csv("data", sep="\s+")
print(df.shape)
print(df)
source = pl.from_pandas(df)
print(source)


chart = alt.Chart(source).mark_bar().encode(
    x='year:O',
    y='yield:Q',
    color='year:Q',  #O, N, Q, T, G
    column='site:N'
)

# yield           variety  year             site

# render in browser
import os, webbrowser as wb
tempFile = "/tmp/chart.html"
chart.save(tempFile)
wb.open(tempFile)
os.system(f"rm {tempFile}")
