############################################################
#
#    exec statements
#
############################################################

# Using eval and exec is regarded as a secut=rity risk these days 

x = 10
y = 20
codeFragment = input("Please enter some code (e.g. 'print x + y'): ")
exec(codeFragment.rstrip())

1
