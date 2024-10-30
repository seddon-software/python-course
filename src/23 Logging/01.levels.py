import os; os.system("clear")
'''

Logging
=======

It is important to add logging to your application, especially if it is going to be run unattended.  In such cases
writing error messages to the console cam easily be missed and besides your log is a permant record of a run.

Python logging is based around the way logging is implemented in Java.  Default logging is very simple but can 
be extensively customised if so desired.

Normally we write messages to a log file, but here we look at the basic ideas behind simple logging using the
console instead of a file.  You should not rely on console logging in a real application.

Default logging defines 5 logging levels:
            DEBUG
            INFO
            WARNING
            ERROR
            CRITICAL

of increasing severity.  In a typical application you set one of these 5 levels at the start of the application
and then periodically log messages during the application.  If you choose DEBUG as the level:
            logging.basicConfig(level=logging.DEBUG)

then all logging messages are logged:
            logging.debug('This is a debug message')
            logging.error('This is an error message')
            logging.info('This is an info message')
            logging.warning('This is a warning message')
            logging.critical('This is a critical error message')

At the other end of the scale, if you choose CRITICAl only critical messages are logged:
            logging.critical('This is a critical error message')

Choose something inbetween and only some messages are logged.  So for INFO we just log:
            logging.info('This is an info message')
            logging.warning('This is a warning message')
            logging.critical('This is a critical error message')

Note: the name of the logger will be "root" by default.  Consult the documentation to see how to change the
name.  
'''

import logging


# as no logfile specified, use the console

# choose only one of these 5 options
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(level=logging.CRITICAL)


# now follows your application code interspersed with logging statements:

# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
logging.debug('This is a debug message')
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
logging.error('This is an error message')
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
logging.info('This is an info message')
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
logging.warning('This is a warning message')
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
logging.critical('This is a critical error message')
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code
# lots of lines of code

