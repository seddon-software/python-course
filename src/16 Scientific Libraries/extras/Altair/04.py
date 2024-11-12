import altair as alt
import polars as pl
import pandas as pd

df = pd.read_csv("data", sep="\s+")
temp = df
chart1 = alt.Chart(temp.loc[temp['yield'] != 'Error', :]).mark_line().encode(
    alt.X('index:T'),
    alt.Y('value:Q'),
    alt.Color('Series:N', legend=alt.Legend(orient='left')),
).properties(
    height=400,
    width=1000
)

chart2 = alt.Chart(temp.loc[temp['yield'] == 'Error', :]).mark_line().encode(
    alt.X('index:T'),
    alt.Y('value:Q'),
    color='Series:N'
).properties(
    height=200,
    width=1000
)

chart3 = alt.Chart(temp.loc[temp['year'] == 'Error', :]).mark_bar().encode(
    alt.X('count()'),
    alt.Y('value:Q', bin=alt.Bin(maxbins=100)),
    alt.Color('Series:N')
).properties(
    height=200,
    width=200
)

chart4 = alt.Chart(temp.loc[temp['year'] != 'Error', :]).mark_bar(opacity=.4).encode(
    alt.X('count()'),
    alt.Y('value:Q', bin=alt.Bin(maxbins=100)),
    alt.Color('Series:N')
).properties(
    height=400,
    width=200
)

graph = alt.vconcat(
    alt.hconcat(
        chart1,
        chart4
        ),
    alt.hconcat(
        chart2,
        chart3
        )
)

# render in browser
import os, webbrowser as wb
tempFile = "/tmp/chart.html"
graph.save(tempFile)
wb.open(tempFile)
os.system(f"rm {tempFile}")
