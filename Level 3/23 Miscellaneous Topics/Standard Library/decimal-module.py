############################################################
#
#    Decimals
#
############################################################

import decimal as d

# factorial
x = 1
for n in range(1, 500):
    x = x * n
print(x)


d.getcontext().prec = 1000
x = d.Decimal("1.0") / d.Decimal("7.0")
y = d.Decimal("1.0").exp()
print(x)
print(y)

ctx = d.Context(prec = 60, rounding = d.ROUND_UP)

z = d.Decimal("1.0").exp(ctx)
print(z)




    
    
