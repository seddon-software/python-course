'''
"subprocess.run()" has many options.  You can capture stdout from a child process without using a pipe as
shown below (a pipe is used behind the scenes).

Note the resonse reurn from "run()" is a "CompletedProcess" object and this contains amongst other things
the stdout from the "run()" command.
'''

import subprocess

# output is returned as bytes and needs to be converted to a string for display
response = subprocess.run('ls -l'.split(), capture_output=True)  # CompletedProcess returned
output = response.stdout
print(f'There are {len(output)} bytes in output')
print(output.decode("utf-8"))

# use universal_newlines=True to return a string instead of bytes
response = subprocess.run('ls -l'.split(), capture_output=True, universal_newlines=True)
output = response.stdout
print(f'There are {len(output)} chars in output')
print(output)
