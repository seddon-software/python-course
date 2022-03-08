import pandas as pd
import numpy as np
import geopandas.datasets
import matplotlib.pyplot as plt
import geopandas.geodataframe as gdf
pd.set_option('display.precision', 1)
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 500)

# setup plot
# fig = plt.figure(figsize=(13,8))
# fig.canvas.manager.set_window_title("GeoPandas")
# ax = plt.gca()
import geopandas as gp
z = gp.read_file("topo_lad.json")
# print(z.head())
# print(z.shape)
print( type(z.geometry)) 
# plt.plot(z)
#z.plot(cmap='terrain')
ax = plt.gca()
ax.set_title("AAAA")
ax.set_aspect(1/np.cos(40.0*np.pi/180.0))
#plt.show()
print(z.sample(5))
print(type(z[["LAD13NM"]]))
df = z[['LAD13NM', 'geometry']]
z = z.drop(columns=['geometry'])
print(z)
print(df)
#    df_of_state = df_of_state.groupby(['State']).aggregate(np.mean)
#gdf_exploded=gdf.explode()

#    korean_golds = medal_table[medal_table.Id == "KOR"]["Gold"].values[0]

z = df[df["LAD13NM"] == 'Darlington']
zz = z[["LAD13NM","geometry"]]
print(type(z))
print(z.shape)
print(zz.shape)
print(type(zz))
print(zz.centroid)

zz = gdf.GeoDataFrame.explode(zz, index_parts=True)
print(type(zz))
print(zz.shape)
print(zz)
print(zz["LAD13NM"].values[0])
zz.plot(ax=plt.gca())
#zz.plot(ax=ax, color='black', cmap='Blues')
#plt.show()
ax1=plt.gca()
zz.plot(ax=ax1, marker='.', markersize=1.0)
#plt.show()
print(zz)
    # annotate map with state names    
ax.annotate(text=zz["LAD13NM"].values[0], xy=(zz.centroid.x, zz.centroid.y),  horizontalalignment='center', fontsize=16)
#zz.apply(zzz, axis=1)

# zz.apply(lambda row: ax.annotate(s="ABC", 
#                                            xy=row.geometry.coords[0], 
#                                            horizontalalignment='center', 
#                                            fontsize=6), axis=1)

print("1: ", z['geometry'].values)
print("2: ", z['geometry'])
print(z['geometry'].area)
#print(z['geometry'].plot())
# df.plot(cmap='Blues')
plt.show()
# import time
# time.sleep(10)
import sys
sys.exit()
for index, row in df.iterrows():   
#    g = list(row['geometry'].geoms)
    g = list(row['geometry'])
    gs = gp.GeoSeries(g)
    ax.plot()
    # print(gs)
    plt.show()
    # for x in gs:
    #     print(x.bounds)
    #     print(type(x), x, end=", ")

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
