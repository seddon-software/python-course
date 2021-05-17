import subprocess

subprocess.call(["ls", "-a", "-l"])

# use split
subprocess.call("ls -a -l".split())


