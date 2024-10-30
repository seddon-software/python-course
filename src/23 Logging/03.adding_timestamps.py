import os; os.system("clear")
'''
Adding Timestamps
=================

You can add timestamps to your log messages by simply by including the timestamp in the message string.
'''

import logging
import datetime
import time
import subprocess

# get current time (formatted)
def getCurrentTime():
    t = time.mktime(time.localtime())
    t = time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
    return t

LOG_FILENAME = 'logs/example.log'

# delete (previous log file)
subprocess.call(f"rm {LOG_FILENAME}", shell=True)

# set debug level
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# log some messages
print("logging messages with timestamps ...")
for messageNo in range(10):
    time.sleep(1)
    logging.debug('This debug message goes to the log file')
    logging.info(f'This message was timed at: {getCurrentTime()}')   # timestamp included in message

# inspect log file
import os
subprocess.call(f"cat {LOG_FILENAME}", shell=True)
