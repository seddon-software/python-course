def Grow(theList, item = 0, extra = []):
    extra.append(item)
    theList.extend(extra)
    print(theList)
    

theList = []

Grow(theList, 1, [9, 10])
Grow(theList)
Grow(theList)
Grow(theList)
Grow(theList)
Grow(theList, 2, [9, 10])
Grow(theList)
