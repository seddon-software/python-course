'''
Create 4x6 array of floats between 3.5 and 5.5.  Display the results to 3 decimal 
places.
'''

import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

a = np.random.random(size=(4,6))
print(a*2+3.5)