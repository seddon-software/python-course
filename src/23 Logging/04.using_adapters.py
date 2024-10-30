'''
Using Adaptors
==============

Adaptors are used to add extra information to your logfiles.  In this example we define two adapters that
provide additional logging information:
            Group
            IP
            User

At run time we use a dict to pass in this extra information.  Notice how this information can be changed mid 
stream.
'''

import logging
import datetime
import os, time
import subprocess

print("Using adaptors ...")
input("continue?")
LOG_FILENAME = 'logs/example.log'

# delete (previous) log file
subprocess.call(f"rm {LOG_FILENAME}", shell=True)

# setup logging with a format defined
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format='''%(levelname)-8s %(asctime)-15s \
                              Group: %(name)s IP: %(ip)-15s User: %(user)-8s %(message)s''')

# define dicts for extra fields
extraInfo1 = {"ip": '192.1.1.52', "user": 'sheila'}
extraInfo2 = {"ip": '192.2.1.103', "user": 'jon'}

# create adapters using this extra information
adapter1 = logging.LoggerAdapter(logging.getLogger('GROUP-1'), extraInfo1)
adapter2 = logging.LoggerAdapter(logging.getLogger('GROUP-2'), extraInfo2)

# log messages
adapter1.info('An info message')
adapter1.debug('A debug message')
adapter1.warning('A warning message')
adapter2.info('An info message')
adapter2.debug('A debug message')
adapter2.warning('A warning message')
subprocess.call(f"cat {LOG_FILENAME}", shell=True)


# now change the extra info mid stream
print("changing extra info ...")
extraInfo1["user"] = 'tom'
extraInfo1["ip"] = '192.1.1.63'
extraInfo2["user"] = 'zoe'
extraInfo2["ip"] = '192.2.1.154'

# and log some more messages
adapter1.info('**** changed extra info ****')
adapter2.info('**** changed extra info ****')
adapter1.warning('A warning message')
adapter2.critical('A critical message')

# inspect log file
time.sleep(5)
os.system("clear")
subprocess.call(f"cat {LOG_FILENAME}", shell=True)
