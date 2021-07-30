############################################################
#
#    raise statements
#
############################################################

array = [0,1,2,3,-4,5,6]

try:
    for x in array:
        if x < 0: 
            raise ValueError("array index is negative!")
        print(array[x], end=' ')
except ValueError as e:
    print(f"\n... entering except block: {e}")


