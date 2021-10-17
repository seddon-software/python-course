import logging
import datetime
import time
import subprocess

# clear log file
LOGFILE = 'logs/example2.log'
subprocess.call(f"rm {LOGFILE}", shell=True)

logging.basicConfig(filename=LOGFILE,
                    level=logging.DEBUG,
                    format='%(levelname)-8s %(asctime)-15s Group: %(name)-5s IP: %(ip)-15s User: %(user)-8s %(message)s')

extraInfo1 = {"ip": '192.1.1.52', "user": 'sheila'}
extraInfo2 = {"ip": '192.2.1.103', "user": 'jon'}
adapter1 = logging.LoggerAdapter(logging.getLogger('GROUP-1'), extraInfo1)
adapter2 = logging.LoggerAdapter(logging.getLogger('GROUP-2'), extraInfo2)

# log messages
adapter1.info('An info message')
adapter1.debug('A debug message')
adapter1.warning('A warning message')
adapter2.info('An info message')
adapter2.debug('A debug message')
adapter2.warning('A warning message')

# change extra info
extraInfo1["user"] = 'tom'
extraInfo1["ip"] = '192.1.1.63'
extraInfo2["user"] = 'zoe'
extraInfo2["ip"] = '192.2.1.154'

# log some more messages
adapter1.info('Another info message')
adapter2.info('An info message')
adapter2.critical('A critical message')

# inspect log file
subprocess.call(f"cat {LOGFILE}", shell=True)
