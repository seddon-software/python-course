import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import geodatasets
import os, subprocess
import subprocess

response = subprocess.run("ls 110m_physical/*.shp", shell=True, capture_output=True, universal_newlines=True)
output = response.stdout
shpFiles = output.splitlines()
for shp in shpFiles:
    print(shp)
    z = geopandas.read_file(shp)
    ax = z.plot(color='white', edgecolor='black')
    plt.show()
    input("continue?")
'''
shapefile_path = "110m_physical/ne_110m_land.shp"
land = geopandas.read_file(shapefile_path)

ax = land.plot(color='white', edgecolor='black')


plt.show()
'''