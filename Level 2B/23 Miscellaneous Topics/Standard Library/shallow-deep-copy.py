import copy

def ShallowCopy():
    # create shallow copy of x (only top level objects copied)
    x = [2, 4, [6, 7, 8], 10]
    y = copy.copy(x)
    
    # modify x => y should changed as well
    x[1] = None
    x[2][0] = None
    
    print("Shallow x:", x)
    print("Shallow y:", y)

def DeepCopy():
    # create deep copy of x (all objects copied)
    x = [2, 4, [6, 7, 8], 10]
    y = copy.deepcopy(x)
    
    # modify x => y should be unchanged
    x[1] = None
    x[2][0] = None

    print("Deep x:", x)
    print("Deep y:", y)


ShallowCopy()
DeepCopy()

1