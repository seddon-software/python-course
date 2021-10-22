import shlex

# If we have a program that prompts for a filename, we need to be careful to check
# that someone doesn't use shell injection

# For example, suppose when prompted for a filename, someone enters:
#       'err.txt; rm -rf ~'

inFile = 'err.txt; rm -rf ~'

# If the progam then tries to long list the file, the command would be:  
command = f'command = ls -l {inFile}'
print(command)

print("\n\nThe progam now has a shell injected string which will delete your home directory when executed:")

print("\n\nHowever, if you quote the input - no problem")
command = f'command = ls -l {shlex.quote(inFile)}'
print(command)


