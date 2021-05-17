'''
Create two vectors representing points in 3D space.
Calculate the distance between the points.
'''
import numpy as np

p1 = np.array([2.5, 4.1, 3.7])
p2 = np.array([5.5, 8.1, 8.7])

distance = np.sqrt(np.dot(p2-p1, p2-p1))
print(distance)
