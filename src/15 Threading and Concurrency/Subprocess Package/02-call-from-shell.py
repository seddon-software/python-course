import subprocess

# When shell=True, the command is passed to the shell for interpretation of shell wildcards etc.
# but be careful of shell injection

subprocess.call("ls -l *.py", shell=True)


