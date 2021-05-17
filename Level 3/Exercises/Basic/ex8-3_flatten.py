def flatten(aList):
    flatList = []      
    for item in aList:
        if (type(item)==list):
            flatList.extend(flatten(item))
        else:
            flatList.append(item)          
    return flatList
  
listA = [[1, 2, 3], [4, 5, 6], 7]
listB = [[1, [2, 3], [4, 5, [6, [7]]]]]

print( flatten(listA) )
print( flatten(listB) )

