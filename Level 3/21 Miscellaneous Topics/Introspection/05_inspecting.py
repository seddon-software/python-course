import inspect, os
import struct

# determine the location of the imported module
print(inspect.getabsfile(struct))


# determine the location of this script
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))
print(path)
