import logging
import datetime
import time

LOG_FILENAME = 'logs/example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logging.debug('This message should go to the log file')
t = time.localtime()
t = time.mktime(t)
logging.info(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

# output appended to 'logs/example.log'