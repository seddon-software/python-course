Z = []
N = 30
for r in range(-N,N):
    for i in range(-N,N):
        Z.append(complex(r,i))

# compute the product of all the complex(r,i) numbers in above range
W = [z1*z2 for z1 in Z for z2 in Z]
W = [w for w in W if w.real == 0]
W = set([w.imag for w in W])

# perform a sieve on numbers in range 1 to 100
I = set(i for i in range(1,100))
D = I.difference(W)
D = sorted(D)
print(D)

