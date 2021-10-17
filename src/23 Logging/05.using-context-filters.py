import logging
import re
import time
import subprocess

# clear log file
LOGFILE = 'logs/example3.log'
subprocess.call(f"rm {LOGFILE}", shell=True)

class ContextFilter(logging.Filter):
    def __init__(self, ip, user):
        self.ip = ip
        self.user = user
    def filter(self, record):
        record.ip = self.ip
        record.user = self.user
        return True

myFormat = '''%(levelname)-8s 
              %(asctime)-15s 
              %(name)-5s 
              IP: %(ip)-15s 
              User: %(user)-8s 
              %(message)s'''
pattern = re.compile(r'\s+')
myFormat = re.sub(pattern, ' ', myFormat) # reformat by stripping spaces
print(f"Format: {myFormat}")

logging.basicConfig(filename = LOGFILE,
                    level = logging.DEBUG,
                    format = myFormat)

myLogger = logging.getLogger("FILTER")
myLogger.addFilter(ContextFilter(ip="192.2.2.53", user="Sheila"))

myLogger.debug('A debug message')
myLogger.debug('A debug message')
myLogger.debug('A debug message')
time.sleep(5)
myLogger.addFilter(ContextFilter(ip="192.1.1.13", user="Tom"))
myLogger.info('An info message')
myLogger.info('An info message')
myLogger.info('An info message')

# output appended to 'logs/example3.log'
subprocess.call(f"cat {LOGFILE}", shell=True)
