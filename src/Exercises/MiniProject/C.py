import pandas as pd
import numpy as np
import geopandas.datasets
import matplotlib.pyplot as plt
import geopandas.geodataframe as gdf
import geopandas

from shapely.geometry import Point, LineString
s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
l = geopandas.GeoSeries(LineString([Point(1, 1), Point(3, 2), Point(2, 3)]))
print(s)
ax = l.plot()
s.plot(ax=ax)
plt.grid(True)
plt.show()

