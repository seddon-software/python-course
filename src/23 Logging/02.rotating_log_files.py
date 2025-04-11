'''
Rotating Log Files
==================
In real applications you will want to write to real files.  Here we choose rotating log files.  When a log file
fills up (<20000 bytes) we move on to the next log file.  The backup count defines how many backup files are used.
When all the files have filled up, the rotation begins again.
'''

import glob         # for wildcards
import logging
import logging.handlers
import os; os.system("clear")

print("\nCreate rotation log files")
input("continue?")

# backup log files will have ".1", ".2", etc post-pended to their name
LOG_FILENAME = 'logs/rotation.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(filename=LOG_FILENAME, maxBytes=20000, backupCount=5)
my_logger.addHandler(handler)

# Log some messages
for i in range(10000):
    my_logger.debug(f'This is a logging message #{i}')

print("\nSee what files have been created")
input("continue?")
import subprocess
subprocess.call("ls -l logs/rotation*", shell=True)

print("\nInspect the last few lines of current logfile")
input("continue?")
subprocess.call("tail logs/rotation.out", shell=True)

