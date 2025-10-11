'''
The process of suspending one thread and reactivating a suspended thread is called a context switch.
Python only allows one thread to execute at a time by implementing the global interpreter lock (GIL). 
The Python switch interval is the maximum time the Python interpreter will allow a thread to execute before a forced context switch.

The GIL used to be released after every 100 byte code instructions in Python 2, but in Python 3 this has been supeceded with a time interval
as shown below.  Note that the context switch will only occur after the current byte code instruction completes.
'''

import sys

# determine context switch interval 
print(f"{sys.getswitchinterval()*1000:.0f} msec")

# change it
sys.setswitchinterval(0.00025)
print(f"{sys.getswitchinterval()*1000:0.2f} msec")
