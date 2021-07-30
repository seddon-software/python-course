import shlex

print("When asked for a filename, input 'filename; rm -rf ~' instead (we won't actually execute this command)")
filename = input("Input a filename: ")#'err.txt; rm -rf ~'
command = 'ls -l {}'.format(filename)

print("The progam now has a shell injected string which will delete your home directory when executed:")
print(command)

print("\n\nHowever, if you quote the input - no problem")
command = 'ls -l {}'.format(shlex.quote(filename))
print(command)


