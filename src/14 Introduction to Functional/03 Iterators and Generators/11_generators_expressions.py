import time

N = 5
generators = [(n**2 for n in range(N)),
              (n**3 for n in range(N)),
              (n**4 for n in range(N))]

# generators allow us to perform different calculations in parallel
# create a round robin scheduler
while(True):
    try:
        for g in generators:
            print(next(g))
            time.sleep(0.5)
    except StopIteration as e:
        break
