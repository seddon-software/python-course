import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plotBarChart(df):
    plt.figure(figsize=(13,8), num='GeoPandas', constrained_layout=True)
    ax = plt.gca()
    ax.set_title("Average Wind Speed")
    ax.set_facecolor("orange")
    df.plot.barh(ax=ax)
    plt.show()

# read in WIND data
WIND_df = pd.read_csv("wtk_site_metadata.csv")

# remove entries where the state is unknown
states = WIND_df[['State', 'wind_speed']][WIND_df['State'] != 'Unknown']
states = states.drop_duplicates()

# use mean() to calculate the average wind speed in each state
wind_speeds = states.groupby(['State']).mean()

# final plot
plotBarChart(wind_speeds.sort_index(ascending=False))
