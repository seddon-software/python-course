import pandas as pd
import numpy as np
import geopandas.datasets
import matplotlib.pyplot as plt

pd.set_option('display.precision', 1)
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 500)

def getGeoDataFrame():
    df = pd.read_csv("wtk_site_metadata.csv")
    
    # convert to a series, removing enties where the state is unknown
    states = df['State'][df['State'] != 'Unknown']
    states = states.drop_duplicates().values
    
    # use aggregate to calculate the centroid of each state
    dfs_of_states = []
    for state in states:
        df_of_state = df[['latitude', 'longitude', 'State']][df['State']==state]
        df_of_state = df_of_state.groupby(['State']).aggregate(np.mean)
        df_of_state['State'] = state
        dfs_of_states.append(df_of_state)
    
    # combine indivual state dataframes
    centroid_for_states = pd.concat(dfs_of_states, ignore_index=True)
    
    # add geometry field
    WIND_gdf = geopandas.GeoDataFrame(
        centroid_for_states, 
        geometry=geopandas.points_from_xy(centroid_for_states.longitude, centroid_for_states.latitude)
        )
    return WIND_gdf

def setupPlot():
    plt.figure(figsize=(13,8))
    figure = plt.gcf()
    figure.canvas.manager.set_window_title('GeoPandas')
    ax = plt.gca()
    ax.set_title("States with WIND Data Points in USA")
    ax.set_facecolor("aqua")
    return ax

def plotCountries(ax):
    # extract maps of USA, Mexico and Canada and plot
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    usa = world[world.name == 'United States of America']
    mexico = world[world.name == 'Mexico']
    canada = world[world.name == 'Canada']
    usa.plot(ax=ax, color='orange', edgecolor='black')
    mexico.plot(ax=ax, color='white', edgecolor='black')
    canada.plot(ax=ax, color='white', edgecolor='black')

def plotWIND_data(ax, WIND_gdf):
    # plot a small marker for each state
    WIND_gdf.plot(ax=ax, color='white', markersize=1.0)
    # annotate map with state names    
    WIND_gdf.apply(lambda row: ax.annotate(text=row.State, 
                                           xy=row.geometry.coords[0], 
                                           horizontalalignment='center', 
                                           fontsize=6), axis=1)

def showPlot(ax):
    # restrict plot to contenental USA and scale for approximate Mercator projection
    ax.set_xlim([-130, -60])
    ax.set_ylim([20, 55])
    ax.set_aspect(2.0)
    plt.show()

def main():
    WIND_gdf = getGeoDataFrame()
    ax = setupPlot()
    plotCountries(ax)
    plotWIND_data(ax, WIND_gdf)
    showPlot(ax)

main()
