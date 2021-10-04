import aa
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

pv = "SR-DI-DCCT-01:SIGNAL"
data = aa.get_values(pv, datetime(2021, 1, 5), 
                         datetime(2021, 2, 5))
data_points = data.values.shape[0]
print(data_points)
X = np.arange(data_points)
Y = data.values.reshape((data_points,))
X = X * 31 / data_points  # convert to days
ax = plt.subplot()        # create single figure with one axis
ax.plot(X, Y)
plt.show()

