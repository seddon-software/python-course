def f(self): 
    return self.x

# set function defaults to point to itself 
f.__defaults__ = (f,)

# define a function attribute
f.x = 17

# now copy and remove the original refeence
b = f
del f

# call function and use defaults to determine self
print(b())  # self not specified

