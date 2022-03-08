import pandas as pd
import numpy as np
import geopandas.datasets
import matplotlib.pyplot as plt

pd.set_option('display.precision', 1)
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 500)

# setup plot
fig = plt.figure(figsize=(13,8))
fig.canvas.manager.set_window_title("GeoPandas")
ax = plt.gca()
ax.set_title("WIND Data Points in Texas")
ax.set_facecolor("aqua")

# read in WIND data and a low res map of the world
WIND_df = pd.read_csv("wtk_site_metadata.csv")
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

# just keep 3 columns
WIND_df = WIND_df[['longitude', 'latitude', 'State']]

# only keep Texas entries
Texas_df = WIND_df[WIND_df.State == 'Texas']

# add a geometry column
Texas_gdf = geopandas.GeoDataFrame(
    Texas_df, geometry=geopandas.points_from_xy(Texas_df.longitude, Texas_df.latitude))

# extract maps of USA, Mexico and Canada and plot
usa = world[world.name == 'United States of America']
mexico = world[world.name == 'Mexico']
canada = world[world.name == 'Canada']
usa.plot(ax=ax, color='orange', edgecolor='black')
mexico.plot(ax=ax, color='white', edgecolor='black')
canada.plot(ax=ax, color='white', edgecolor='black')

# plot points from GeoDataFrame
Texas_gdf.plot(ax=ax, color='blue', markersize=0.01)
ax.set_xlim([-130, -60])
ax.set_ylim([20, 55])

# change the aspect ratio because latitude needs scaling to Mercator
# but setting up a custom scale is too complicated
# the scaling will be correct for 40 degrees latitude
ax.set_aspect(1/np.cos(40.0*np.pi/180.0))

plt.show()
