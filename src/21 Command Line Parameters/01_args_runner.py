import subprocess

# clear log file
LOGFILE = 'logs/example3.log'
subprocess.call("python 01_args.py red orange yellow green blue indigo violet", shell=True)


