'''
Adding Timestamps
=================

You can add timestamps to your log messages by simply by including the timestamp in the message string.
'''

import logging
import datetime
import time
import subprocess


LOG_FILENAME = 'logs/example.log'

# delete log file
subprocess.call(f"rm {LOG_FILENAME}", shell=True)

# get current time (formatted)
t = time.mktime(time.localtime())
t = time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))

# set debug level
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# log some messages
logging.debug('This debug message goes to the log file')
logging.info(f'This message was timed at: {t}')   # timestamp included in message

# inspect log file
import os
subprocess.call(f"cat {LOG_FILENAME}", shell=True)
