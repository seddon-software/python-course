import aa
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

pv = "SR-DI-DCCT-01:SIGNAL"
h1 = 0
h2 = 23
data = aa.get_values(pv, datetime(2021, 1, 5, hour=h1, minute=0), 
                         datetime(2021, 1, 5, hour=h2, minute=0))
data_points = data.values.shape[0]
X = np.arange(h1, h2, (h2-h1)/data_points)
Y = data.values.reshape((data_points,))
ax = plt.subplot()      # create single figure with one axis
ax.plot(X, Y)
plt.show()

