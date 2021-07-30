############################################################
#
#    deep copies
#
############################################################

import numpy as np

a = np.arange(12); print(a)
b = a.copy(); print(b)

# changes to a do not affect b
a[3] = 99
print(a)
print(b)

1
