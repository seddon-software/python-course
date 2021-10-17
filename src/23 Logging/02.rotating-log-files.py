import glob
import logging
import logging.handlers

LOG_FILENAME = 'logs/rotation.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=20000, backupCount=5)

my_logger.addHandler(handler)

# Log some messages
for i in range(10000):
    my_logger.debug(f'This is a logging message {i}')

# See what files are created
import subprocess
subprocess.call("ls -l logs/rotation*", shell=True)

