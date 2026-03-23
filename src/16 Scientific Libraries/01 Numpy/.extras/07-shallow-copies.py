############################################################
#
#    shallow copies
#
############################################################

import numpy as np

a = np.arange(12); print(a)
b = a
print(a is b)

c = a.view()    # a and c point to different arrays that share data
print(a is c)

# change underlying data - both arrays see the changes
a[3] = 99
print(a)
print(b)
print(c)

# reshape one array - data unchanged
c.shape = 3,4
print(a)
print(c)

# slice creates a view
d = a[2:5]; print(d)
a[3] = 88
print(d) # sees the change to a





1
