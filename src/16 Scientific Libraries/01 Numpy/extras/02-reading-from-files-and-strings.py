import numpy as np
import io

# data can be tab separated or comma seperated  

# read data from a file (tab seperated)  
data = np.genfromtxt('files/test1.dat')
np.set_printoptions(precision=3)
np.set_printoptions(formatter={'float': lambda x: "{:8.1f}".format(x)})
print(data)

# read data from byte stream (comma separated)
input=b"""        # must be byte stream
1, 23.7, Monday\n
2, 14.6, Tuesday\n
3, 18.9, Wednesday\n
4, 25.1, Thursday\n
5, 17.3, Friday\n
"""
raw_data = io.BytesIO(input)
data = np.genfromtxt(raw_data, dtype="i8,f8,S3", delimiter=", ")

for row in data:
    print(row)

