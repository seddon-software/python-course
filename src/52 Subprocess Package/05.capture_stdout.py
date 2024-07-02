'''
"subprocess.run()" has many options.  You can capture stdout from a child process without using a pipe as
shown below (a pipe is used behind the scenes).

Note the resonse return from "run()" is a "CompletedProcess" object and this contains amongst other things
the stdout from the "run()" command.

By default the response is in bytes (which we decode to a 'utf-8' string), but by using 'universal_newlines' 
the response is automatically converted to a 'utf-8' string.
'''

import subprocess

# output is returned as bytes and needs to be converted to a string for display
response = subprocess.run('ls -l'.split(), capture_output=True)  # CompletedProcess returned
output = response.stdout
print(output)
print(f'There are {len(output)} bytes in output')
print(output.decode("utf-8"))

# use universal_newlines=True to return a string instead of bytes
response = subprocess.run('ls -l'.split(), capture_output=True, universal_newlines=True)
output = response.stdout
print(f"Universal lines return: {type(output)}")
print(output)
