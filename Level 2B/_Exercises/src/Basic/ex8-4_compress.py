def compress(aList):
      return [item for i, item in enumerate(aList) if i==0 or item != aList[i-1]]
  
print( compress([4,7,5,5,5,3,4,4,4,2,2]) )