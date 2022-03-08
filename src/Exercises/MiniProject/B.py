from shapely.geometry import *
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
p = Polygon([(0, 5),
   (1, 1),
   (3, 0),
   (4, 6),
])
line2 = LineString([Point(0, 0), Point(3, 1), Point(2, 3)])
x, y = p.exterior.xy
print(x, y)
print(line2.xy)
print(line2.wkt)
plt.plot(line2, c="black")
plt.plot(x, y, c="red")
plt.grid(True)
plt.show()
