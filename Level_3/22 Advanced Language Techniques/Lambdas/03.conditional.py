
# the lambda will capture variable a
a = 37
f = (lambda x,y:x+y+a) if a > 20 else (lambda x,y:x-y+a) 

print((f(5,2)))
print((f(15,2)))

a = 100
print((f(5,2)))        # uses current value of a
print((f(15,2)))

1