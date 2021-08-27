import aa
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np



event = aa.get_value_at('SR-DI-DCCT-01:SIGNAL', datetime.now())
print(event.value)
pv = "SR-DI-DCCT-01:SIGNAL"
data = aa.get_values(pv, datetime(2021, 1, 5, hour=13, minute=0), datetime(2021, 1, 5, hour=14, minute=0))
#print(data.values)
data_points = data.values.shape[0]
X = np.arange(data_points)
Y = data.values.reshape((data_points,))
print(X.shape, Y.shape)
ax = plt.subplot()      # create single figure with one axis
redCircles = "ro"
ax.plot(X, Y)
# ax.plot(X, Y, redCircles)
plt.show()

