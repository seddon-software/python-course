import numpy as np
import matplotlib.pyplot as plt

import numpy as np
s = np.random.exponential(1, 1000)

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 25)
plt.show()
