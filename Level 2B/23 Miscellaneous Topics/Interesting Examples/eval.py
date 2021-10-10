############################################################
#
#    eval operators
#
############################################################

# Using eval and exec is regarded as a secut=rity risk these days 

x = 10
y = 20
codeFragment = input("Please enter an expression (e.g. 'x + y'): ")

result = eval(codeFragment.rstrip())
print("result is: ", result)

