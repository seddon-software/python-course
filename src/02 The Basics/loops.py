############################################################
#
#    loops
#
############################################################

# standard
for x in range(1,10):
    print(x, end=' ')

# for with else
for x in (1,2,3,4,5,6):
    print(x, end=' ')
    if x > 3: break
else:
    print("only get here if all iterations succeed ...")

# while
formula = 0
x = 0

while formula < 1000:
    formula = 2*x*(x + 1)
    x = x + 1
    print(x, formula)
