import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plotBarChart(df):
    plt.figure(figsize=(13,8), num='GeoPandas')
    ax = plt.gca()
    ax.set_title("Average Wind Speed")
    ax.set_facecolor("orange")
    df.plot.barh(ax=ax)
    plt.show()

pd.set_option('display.precision', 1)
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 500)

# read in WIND data
WIND_df = pd.read_csv("wtk_site_metadata.csv")
print(WIND_df)
print(WIND_df.sample(5))

WIND_df2 = WIND_df.groupby(['State']).aggregate(np.mean)
WIND_df2 = WIND_df2[['wind_speed']]
print(WIND_df2)
plotBarChart(WIND_df2.sort_index(ascending=False))