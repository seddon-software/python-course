import time

generators = [(n**2 for n in range(50)),
              (n**3 for n in range(50)),
              (n**4 for n in range(50))]

# generators allow us to perform different calculations in parallel
# create a round robin scheduler
while(True):
    for g in generators:
        print(next(g))
        time.sleep(0.5)

