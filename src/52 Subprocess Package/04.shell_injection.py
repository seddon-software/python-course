'''
Shell Injection
===============
Shell injection or command injection occurs when your program accepts unparsed input froma malicious user.  In
the example below we demonstrate (safetly!) how this works.  The program prompts for a filename, but the 
malicious user enters a filename followed by a semi colon.  The semi-colon is the command separator on Linux, so
whatever follows the semi-colon will be executed as in addition command in this example.

The shlex cpmmand protects against this type of attack by surrounding the user input with quotes.  This time the shell 
looks for a filename that includes the whole user input including the semi colon and almost certainly won't find such a 
filename and hence the shell generates an error - no damage done!
'''

import shlex

# If we have a program that prompts for a filename, we need to be careful to check
# that someone doesn't use shell injection

# For example, suppose when prompted for a filename, someone enters:
#       'err.txt; rm -rf ~'

inFile = 'err.txt; rm -rf ~'

# If the progam then tries to long list the file, the command would be:  
command = f'command = ls -l {inFile}'

print("\n\nThe progam now has a shell injected string which will delete your home directory when executed:")
print(command)

print("\n\nHowever, if you quote the input using 'shlex' - no problem")
command = f'command = ls -l {shlex.quote(inFile)}'
print(command)


