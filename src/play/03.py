p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

for p1 in p:
    p2 = [x for x in p if x < p1]
    print(f"{p1:3}: ", end="")
    for p3 in p2:
#        print(f"{p3:2}({p1%p3:2})", end=",")
        print(f"{p1%p3:2}", end=",")
    print()
