calc = lambda : {
  '*': lambda : x * 5,
  '+': lambda : x + 5,
  '-': lambda : x - 5
  }[op]()

op = '+'
x = 100
print(calc())
x = 200
print(calc())
op = '-'
print(calc())
op = '*'
print(calc())
1
