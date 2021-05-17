import subprocess

# output is returned as bytes and need to be converted to a string to display
output = subprocess.check_output('ls -l'.split())
print(f'There are {len(output)} bytes in output')
print(output.decode("utf-8"))

# use universal_newlines=True to return a string
output = subprocess.check_output('ls -l'.split(), universal_newlines=True)
print(f'There are {len(output)} chars in output')
print(output)
