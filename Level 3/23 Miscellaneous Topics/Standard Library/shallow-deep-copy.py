import copy

def ShallowCopy():
    # create shallow copy of x (only top level objects copied)
    x = [1, 2, 3, 4, [5, 6, 7, 8], 9, 10]
    y = copy.copy(x)
    
    x[0] = 99         # this doesn't change y because its top level
    print(f"top level:  x[0]={x[0]}, y[0]={y[0]}")
    x[4][0] = 88      # this DOES change y because its one level down
    print(f"one level down:  x[4][0]={x[4][0]}, y[4][0]={y[4][0]}")

    print("Shallow x:", x)
    print("Shallow y:", y)

def DeepCopy():
    # create deep copy of x (all objects copied)
    x = [1, 2, 3, 4, [5, 6, 7, 8], 9, 10]
    y = copy.deepcopy(x)
    
    # modify x => y should be unchanged
    x[0] = 99
    print(f"top level:  x[0]={x[0]}, y[0]={y[0]}")
    x[4][0] = 88
    print(f"one level down:  x[4][0]={x[4][0]}, y[4][0]={y[4][0]}")

    print("Deep x:", x)
    print("Deep y:", y)


ShallowCopy()
DeepCopy()

