N = 100
NR = int(N**0.5)
products = [n*(x+1) for n in range(2,N) for x in range(1,NR+1)]
products2 = [n for n in products if products.count(n) > 1]
z = [n for n in range(2, N) if n not in products2]
print(z)
zz = [n for n in range(2,N) if n not in z]
print(zz)